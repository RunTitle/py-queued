# _*_ coding: utf-8

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
    def __init__(
            self, config, aws_owner, aws_access_key_id, aws_secret_access_key,
            application, subscriptions=[], publications=[], bucket=None
    ):
        self.config = BASE_CONFIG.copy()
        self.config.update(config)
        self.aws_owner = aws_owner
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.application = application
        self.subscriptions = subscriptions
        self.publications = publications
        self.env = self.config['env']
        self.region = self.config['region']
        self.maxSize = self.config['maxSize']
        self.bucket = bucket
        if self.bucket is None:
            self.bucket = 'queued-' + self.env
