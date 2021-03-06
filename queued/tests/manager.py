import os
import unittest

from ..manager import QueuedManager
from .test_data import STANDARD_DATA


class TestQueuedManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.aws_owner = os.environ.get('AWS_OWNER')
        cls.aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
        cls.aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
        cls.sns_name = 'arn:aws:sns:us-east-1:' + cls.aws_owner + ':rtq-test-value'
        cls.sqs_name = 'arn:aws:sqs:us-east-1:' + cls.aws_owner + ':rtq-test-value-queued'
        cls.application = 'queued'
        cls.subscriptions = ['parsley']
        cls.publications = ['parsley']
        cls.queued_manager = QueuedManager(
            config={}, aws_owner=cls.aws_owner, application=cls.application,
            aws_access_key_id=cls.aws_access_key_id,
            aws_secret_access_key=cls.aws_secret_access_key,
            publications=cls.publications, subscriptions=cls.subscriptions
        )

    def test_sns_name(self):
        self.assertEqual(self.queued_manager.sns_name('value'), 'rtq-test-value')

    def test_sqs_name(self):
        self.assertEqual(self.queued_manager.sqs_name('value'), 'rtq-test-value-queued')

    def test_arn_name(self):
        self.assertEqual(self.queued_manager.arn_name('value', 'sns'), self.sns_name)
        self.assertEqual(self.queued_manager.arn_name('value', 'sqs'), self.sqs_name)

    def test_delete_nonexistant_queue(self):
        self.assertFalse(self.queued_manager.delete_queue('bananas'))

    def test_delete_nonexistant_topic(self):
        self.assertFalse(self.queued_manager.delete_topic('bananas'))

    def test_get_topic(self):
        self.assertTrue(self.queued_manager.get_topic(self.publications[0]))

    def test_get_queue(self):
        self.assertTrue(self.queued_manager.get_queue(self.subscriptions[0]))

    def test_publish_message(self):
        self.assertTrue(self.queued_manager.publish_message(self.publications[0], STANDARD_DATA))

    def test_receive_message(self):
        message = self.queued_manager.receive_message(self.subscriptions[0])
        content = self.queued_manager.messages.decode(message)
        self.assertTrue('doc_type' in content)
        self.assertFalse(self.queued_manager.remove_message(self.subscriptions[0], message))

    @classmethod
    def tearDownClass(cls):
        cls.queued_manager.delete_queue(cls.subscriptions[0])
        cls.queued_manager.delete_topic(cls.publications[0])
