import json
import os

from boto.s3.connection import S3Connection
from boto.s3.key import Key


class Storage:
    STORAGE_KEY_SCALES = 'scales'
    STORAGE_KEY_HANON = 'hanon'
    STORAGE_KEY_BLUES = 'blues'


    @staticmethod
    def get_data_as_json(key):
        bucket = Storage.storage_bucket()
        scales_storage = Key(bucket)
        scales_storage.key = key
        return json.loads(scales_storage.get_contents_as_string())


    @staticmethod
    def get_scales_as_json():
        print('Storage.get_scales')
        print('Storage.get_scales: Storage.get_data(Storage.STORAGE_KEY_SCALES): ' + str(Storage.get_data_as_json(Storage.STORAGE_KEY_SCALES)))
        return Storage.get_data_as_json(Storage.STORAGE_KEY_SCALES)


    @staticmethod
    def get_scales_as_string():
        return json.dumps(Storage.get_scales_as_json())


    @staticmethod
    def set_scales_from_string(scales):
        bucket = Storage.storage_bucket()
        scales_storage = Key(bucket)
        scales_storage.key = Storage.STORAGE_KEY_SCALES
        scales_storage.set_contents_from_string(scales)


    @staticmethod
    def set_hanon_from_string(hanon):
        bucket = Storage.storage_bucket()
        scales_storage = Key(bucket)
        scales_storage.key = Storage.STORAGE_KEY_HANON
        scales_storage.set_contents_from_string(hanon)


    @staticmethod
    def set_blues_from_string(blues):
        bucket = Storage.storage_bucket()
        scales_storage = Key(bucket)
        scales_storage.key = Storage.STORAGE_KEY_HANON
        scales_storage.set_contents_from_string(blues)


    @staticmethod
    def get_hanon_as_json():
        return Storage.get_data_as_json(Storage.STORAGE_KEY_HANON)


    @staticmethod
    def get_hanon_as_string():
        return json.dumps(Storage.get_hanon_as_json())


    @staticmethod
    def get_blues_as_json():
        return Storage.get_data_as_json(Storage.STORAGE_KEY_BLUES)


    @staticmethod
    def get_blues_as_string():
        return json.dumps(Storage.get_blues_as_json())


    @staticmethod
    def read_from_storage(storage_key):
        b = Storage.storage_bucket()
        scales = Key(b)
        scales.key = storage_key
        content = scales.get_contents_as_string()
        return json.loads(content)


    @staticmethod
    def storage_bucket():
        apikey = os.environ['CELLAR_ADDON_KEY_ID']
        secretkey = os.environ['CELLAR_ADDON_KEY_SECRET']
        host = os.environ['CELLAR_ADDON_HOST']
        conn = S3Connection(aws_access_key_id=apikey, aws_secret_access_key=secretkey, host=host)
        return conn.get_bucket('exercises')