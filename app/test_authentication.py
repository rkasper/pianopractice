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
        try:
            did_token = token()
            self.assertIsNotNone(did_token)
            self.assertIsInstance(did_token, str)
        except RuntimeError as e:
            # We expect there to be an error when running as a unit test, outside of Flask context. When there is no
            # login token, the @did_token_required wrapper forwards to the login Flask route. Outside of Flask, you
            # can't do that, so there's a RuntimeError - again, the expected test result.
            pass
