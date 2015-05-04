# _*_ coding: utf-8


def QueuedBase(object):
    def __init__(self, environment, application, region='us-east-1'):
        self.environment = environment
        self.application = application
        self.region = region
        self.maxSize = 262144
