# _*_ coding: utf-8
from .base import QueuedBase


class QueuedMessage(QueuedBase):
    def _create_bucket(self):
        pass

    def _put_S3(self, msg):
        pass

    def create(self, msg):
        pass

    def decode(self, msg):
        pass
