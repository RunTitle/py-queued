# _*_ coding: utf-8

import boto3

BASE_CONFIG = {
    'env': 'test',
    'region': 'us-east-1',
    's3ApiVersion': '2006-03-01',
    'sqsApiVersion': '2012-11-05',
    'snsApiVersion': '2010-03-31',
    'sqsListnerDefaults': {
        'MaxNumberOfMessages': 1,
        'VisibilityTimeout': 60,
        'WaitTimeSeconds': 10
    },
    'maxSize': 262144,
}


class QueuedBase(object):
    def __init__(self, config, application, aws_owner=None, aws_access_key_id=None, aws_secret_access_key=None, subscriptions=[], publications=[], bucket=None):
        self.config = BASE_CONFIG.copy()
        self.config.update(config)
        self.application = application
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.subscriptions = subscriptions
        self.publications = publications
        self.env = self.config['env']
        self.region = self.config['region']
        self.maxSize = self.config['maxSize']
        self.bucket_name = bucket
        if self.bucket_name is None:
            self.bucket_name = 'queued-' + self.env
        self.aws_owner = aws_owner
        if not self.aws_owner:
            # Request account id from Simple Token Service
            # As of right now, we either provide the aws_owner in the config, or we're
            # running on lambda, so if we get here we know that we're in lambda land
            # and therefore have access to STS
            self.aws_owner = boto3.client('sts').get_caller_identity().get('Account')
