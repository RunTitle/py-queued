import os
import json
import unittest
from boto.sqs.message import Message

from ..messages import QueuedMessage
from .test_data import STANDARD_DATA, LARGE_DATA


class TestQueuedMessages(unittest.TestCase):
    def setUp(self):
        self.owner = os.environ.get('AWS_OWNER')
        self.application = 'queued'
        self.subscriptions = ['parsley']
        self.publications = ['parsley']
        self.queued_message = QueuedMessage(
            config={}, owner=self.owner, application=self.application,
            publications=self.publications, subscriptions=self.subscriptions
        )

    def test_encode_standard(self):
        message = self.queued_message.create(STANDARD_DATA)
        decoded_message = self.queued_message.decode(
            Message(body=json.dumps({'Message': message})))
        self.assertTrue(decoded_message.get('doc_type'))

    def test_encode_large(self):
        message = self.queued_message.create(LARGE_DATA)
        self.assertEqual(json.loads(message)['Bucket'], self.queued_message.bucket)
        decoded_message = self.queued_message.decode(
            Message(body=json.dumps({'Message': message})))
        self.assertTrue(decoded_message.get('details'))
