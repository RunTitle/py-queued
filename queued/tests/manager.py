import os
import unittest

from ..manager import QueuedManager
from .test_data import STANDARD_DATA


class TestQueuedManager(unittest.TestCase):
    def setUp(self):
        self.owner = os.environ.get('AWS_OWNER')
        self.sns_name = 'arn:aws:sns:us-east-1:' + self.owner + ':rtq-test-value'
        self.sqs_name = 'arn:aws:sqs:us-east-1:' + self.owner + ':rtq-test-value-queued'
        self.application = 'queued'
        self.subscriptions = ['parsley']
        self.publications = ['parsley']
        self.queued_manager = QueuedManager(
            config={}, owner=self.owner, application=self.application,
            publications=self.publications, subscriptions=self.subscriptions
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

    def tearDown(self):
        self.queued_manager.delete_queue(self.subscriptions[0])
        self.queued_manager.delete_topic(self.publications[0])
