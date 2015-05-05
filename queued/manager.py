# _*_ coding: utf-8
from .base import QueuedBase


class QueuedManager(QueuedBase):
    def __init__(self, *args, **kwargs):
        super(QueuedManager, self).__init__(*args, **kwargs)
        self._init_publications()
        self._init_subscriptions()

    def _init_publications(self):
        pass

    def _init_subscriptions(self):
        pass

    def sqs_name(self):
        pass

    def sns_name(self):
        pass

    def arn_name(self, env):
        return env

    def get_queue_url(self):
        pass

    def get_queue_name(self):
        pass

    def authorize_sns(self):
        pass

    def get_topic(self):
        pass

    def delete_topic(self):
        pass

    def get_queue(self):
        pass

    def delete_queue(self):
        pass

    def publish_message(self):
        pass

    def receive_message(self):
        pass

    def remove_message(self):
        pass
