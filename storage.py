import json
import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key


class Storage:
    STORAGE_KEY_SCALES = 'scales'
    STORAGE_KEY_HANON = 'hanon'
    STORAGE_KEY_BLUES = 'blues'

    @staticmethod
    def storage_bucket():
        apikey = os.environ['CELLAR_ADDON_KEY_ID']
        secretkey = os.environ['CELLAR_ADDON_KEY_SECRET']
        host = os.environ['CELLAR_ADDON_HOST']
        conn = S3Connection(aws_access_key_id=apikey, aws_secret_access_key=secretkey, host=host)
        return conn.get_bucket('exercises')

    @staticmethod
    def get_data_as_json(key):
        bucket = Storage.storage_bucket()
        content_storage = Key(bucket)
        content_storage.key = key
        return json.loads(content_storage.get_contents_as_string())

    @staticmethod
    def set_content_from_string(key, content):
        bucket = Storage.storage_bucket()
        content_storage = Key(bucket)
        content_storage.key = key
        content_storage.set_contents_from_string(content)

    @staticmethod
    def get_scales_as_json():
        return Storage.get_data_as_json(Storage.STORAGE_KEY_SCALES)

    @staticmethod
    def get_scales_as_string():
        return json.dumps(Storage.get_scales_as_json())

    @staticmethod
    def set_scales_from_string(scales):
        Storage.set_content_from_string(Storage.STORAGE_KEY_SCALES, scales)

    @staticmethod
    def get_hanon_as_json():
        return Storage.get_data_as_json(Storage.STORAGE_KEY_HANON)

    @staticmethod
    def get_hanon_as_string():
        return json.dumps(Storage.get_hanon_as_json())

    @staticmethod
    def set_hanon_from_string(hanon):
        Storage.set_content_from_string(Storage.STORAGE_KEY_HANON, hanon)

    @staticmethod
    def get_blues_as_json():
        return Storage.get_data_as_json(Storage.STORAGE_KEY_BLUES)

    @staticmethod
    def get_blues_as_string():
        return json.dumps(Storage.get_blues_as_json())

    @staticmethod
    def set_blues_from_string(blues):
        Storage.set_content_from_string(Storage.STORAGE_KEY_BLUES, blues)
