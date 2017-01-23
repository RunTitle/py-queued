# _*_ coding: utf-8
import boto
import boto3
import json
import uuid
from boto.s3.key import Key

from .base import QueuedBase


class QueuedMessage(QueuedBase):
    def __init__(self, *args, **kwargs):
        super(QueuedMessage, self).__init__(*args, **kwargs)
        self.bucket_conn = None
        self.conn = boto.connect_s3(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key)
        self._create_bucket()

    def _create_bucket(self):
        self.bucket_conn = self.conn.create_bucket(self.bucket_name)

    def _put_S3(self, msg):
        key = '/'.join([self.application, uuid.uuid4().hex])
        key_object = Key(self.bucket_conn)
        key_object.key = key
        key_object.content_type = 'application/json'
        key_object.set_contents_from_string(msg)
        key_object.close()
        return json.dumps({'Bucket': self.bucket_name, 'Key': key})

    def create(self, msg):
        message = json.dumps(msg)
        if len(message) >= self.maxSize:
            return self._put_S3(message)
        return message

    def decode(self, msg):
        content = json.loads(msg.get_body())
        details = json.loads(content['Message'])
        if 'Bucket' in details and 'Key' in details:
            key_object = Key(self.conn.get_bucket(details['Bucket']))
            key_object.key = details['Key']
            return json.loads(key_object.get_contents_as_string())
        return details

class QueuedLambdaMessage(QueuedBase):
    def __init__(self, *args, **kwargs):
        super(QueuedLambdaMessage, self).__init__(*args, **kwargs)
        self.s3 = boto3.resource('s3')
        self.bucket = self.s3.Bucket(self.bucket_name)
        self.bucket.create()

    def _put_S3(self, msg):
        key = '/'.join([self.application, uuid.uuid4().hex])
        self.s3.Object(self.bucket_name, key).put(Body=msg)
        return json.dumps({'Bucket': self.bucket_name, 'Key': key})

    def create(self, msg):
        message = json.dumps(msg)
        if len(message) >= self.maxSize:
            return self._put_S3(message)
        return message

    def decode(self, msg):
        content = json.loads(msg.get_body())
        details = json.loads(content['Message'])
        if 'Bucket' in details and 'Key' in details:
            obj = self.s3.Object(details['Bucket'], details['Key'])
            return json.loads(obj.get())
        return details
