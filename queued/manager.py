# _*_ coding: utf-8
import boto3

from .base import QueuedBase
from .messages import QueuedMessage, QueuedLambdaMessage

class BaseQueuedManager(QueuedBase):
    def __init__(self, *args, **kwargs):
        super(BaseQueuedManager, self).__init__(*args, **kwargs)
        self._cache = {'queues': {}, 'topics': {}}
        self.sqs = boto3.resource('sqs', region_name=self.region)
        self.sns = boto3.resource('sns', region_name=self.region)
        self._init_publications()
        self._init_subscriptions()

    def _init_publications(self):
        for publication in self.publications:
            self.get_topic(publication)

    def _init_subscriptions(self):
        for subscription in self.subscriptions:
            self.subscribe_topic(subscription)

    def sqs_name(self, name):
        return '-'.join(['rtq', self.env, name, self.application])

    def sns_name(self, name):
        return '-'.join(['rtq', self.env, name])

    def arn_name(self, name, arn_type):
        if arn_type == 'sns':
            return ':'.join(
                ['arn', 'aws', arn_type, self.region, self.aws_owner, self.sns_name(name)])

        return ':'.join(['arn', 'aws', arn_type, self.region, self.aws_owner, self.sqs_name(name)])

    def subscribe_topic(self, name):
        topic = self.sns.Topic(self.arn_name(name, 'sns'))
        topic.subscribe(Protocol='sqs', Endpoint=self.get_queue(name))

    def get_topic(self, name):
        return self.sns.create_topic(Name=self.sns_name(name))

    def delete_topic(self, name):
        self.sns.delete_topic(self.arn_name(name, 'sns'))

    def get_queue(self, name):
        queue_name = self.sqs_name(name)
        return self._cache['queues'].get(queue_name, self.sqs.create_queue(queue_name))

    def delete_queue(self, name):
        queue = self.sqs.get_queue(self.sqs_name(name))
        if queue is not None:
            queue.delete()

    def publish_message(self, name, raw_message):
        msg = self.messages.create(raw_message)
        topic = self.sns.Topic(self.arn_name(name, 'sns'))
        return topic.publish(TopicArn=self.arn_name(name, 'sns'), Message=msg)

    def receive_message(self, name):
        queue = self.get_queue(name)
        if queue is None:
            return

        messages = queue.get_messages(
            num_messages=self.config['sqsListnerDefaults']['MaxNumberOfMessages'],
            visibility_timeout=self.config['sqsListnerDefaults']['VisibilityTimeout'],
            wait_time_seconds=self.config['sqsListnerDefaults']['WaitTimeSeconds'],
        )
        if messages:
            return messages[0]

    def remove_message(self, name, message):
        queue = self.sqs.get_queue(self.sqs_name(name))
        if queue is not None:
            queue.delete_message(message)

# It would probably be better if this were named something like DefaultQueuedManager,
# or CredentialedQueueManager. However, that would require changing the name for all
# current users.
class QueuedManager(BaseQueuedManager):
    def __init__(self, *args, **kwargs):
        super(QueuedManager, self).__init__(*args, **kwargs)
        self.messages = QueuedMessage(*args, **kwargs)

class LambdaQueuedManager(BaseQueuedManager):
    def __init__(self, *args, **kwargs):
        super(LambdaQueuedManager, self).__init__(*args, **kwargs)
        self.messages = QueuedLambdaMessage(*args, **kwargs)
