import json
import unittest
import warnings
from os import environ

from storage import Storage


class StorageTests(unittest.TestCase):
    def ignore_warnings(test_method):
        def test_run(self, *args, **kwargs):
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                test_method(self, *args, **kwargs)

        return test_run

    @ignore_warnings
    def test_canGetScalesFromStorage(self):
        content_as_string = Storage.get_scales_as_string()
        self.assertTrue(len(content_as_string) > 0)

        content_as_json = Storage.get_scales_as_json()
        self.assertTrue(len(content_as_json) > 0)

        self.assertEqual(json.loads(content_as_string), content_as_json)

    @ignore_warnings
    def test_canGetHanonFromStorage(self):
        content_as_string = Storage.get_hanon_as_string()
        self.assertTrue(len(content_as_string) > 0)

        content_as_json = Storage.get_hanon_as_json()
        self.assertTrue(len(content_as_json) > 0)

        self.assertEqual(json.loads(content_as_string), content_as_json)

    @ignore_warnings
    def test_canGetBluesFromStorage(self):
        content_as_string = Storage.get_blues_as_string()
        self.assertTrue(len(content_as_string) > 0)

        content_as_json = Storage.get_blues_as_json()
        self.assertTrue(len(content_as_json) > 0)

        self.assertEqual(json.loads(content_as_string), content_as_json)

    @unittest.skipUnless(environ.get('MOCK_DB'), "Only test with mock DB - don't break the production DB.")
    def test_canSetScalesToStorage(self):
        original_content = Storage.get_scales_as_string()
        new_content = '["poop"]'
        Storage.set_scales_from_string(new_content)
        self.assertEqual(new_content, Storage.get_scales_as_string())
        Storage.set_scales_from_string(original_content)

    @unittest.skipUnless(environ.get('MOCK_DB'), "Only test with mock DB - don't break the production DB.")
    def test_canSetHanonToStorage(self):
        original_content = Storage.get_hanon_as_string()
        new_content = '["poop"]'
        Storage.set_hanon_from_string(new_content)
        self.assertEqual(new_content, Storage.get_hanon_as_string())
        Storage.set_hanon_from_string(original_content)

    @unittest.skipUnless(environ.get('MOCK_DB'), "Only test with mock DB - don't break the production DB.")
    def test_canSetBluesToStorage(self):
        original_content = Storage.get_blues_as_string()
        new_content = '["poop"]'
        Storage.set_blues_from_string(new_content)
        self.assertEqual(new_content, Storage.get_blues_as_string())
        Storage.set_blues_from_string(original_content)