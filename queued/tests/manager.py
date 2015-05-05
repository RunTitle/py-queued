import os
import unittest

from ..manager import QueuedManager


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
