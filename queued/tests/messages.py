import os
import json
import unittest
from boto.sqs.message import Message

from ..messages import QueuedMessage
from .test_data import STANDARD_DATA, LARGE_DATA


class TestQueuedMessages(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.aws_owner = os.environ.get('AWS_OWNER')
        cls.aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        cls.aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        cls.application = 'queued'
        cls.subscriptions = ['parsley']
        cls.publications = ['parsley']
        cls.queued_message = QueuedMessage(
            config={}, aws_owner=cls.aws_owner, application=cls.application,
            aws_access_key_id=cls.aws_access_key_id,
            aws_secret_access_key=cls.aws_secret_access_key,
            publications=cls.publications, subscriptions=cls.subscriptions
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
