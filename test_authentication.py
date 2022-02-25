import unittest

from authentication import with_magic_publishable_api_key, did_token_required


@with_magic_publishable_api_key
def key(magic_publishable_api_key):
    return magic_publishable_api_key


@did_token_required
def token(did_token):
    return did_token


class AuthenticationTests(unittest.TestCase):
    def test_hasMagicPublishableKey(self):
        magic_publishable_api_key = key()
        self.assertIsNotNone(magic_publishable_api_key)
        self.assertIsInstance(magic_publishable_api_key, str)

    def test_hasDidToken(self):
        did_token = token()
        self.assertIsNotNone(did_token)
        self.assertIsInstance(did_token, str)
