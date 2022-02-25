import os
from functools import wraps

from flask import request, redirect, url_for
from magic_admin import Magic


def __get_magic_secret_key():
    return os.environ.get('MAGIC_SECRET_KEY')


def with_magic_publishable_api_key(func):
    @wraps(func)
    def inject_magic_publishable_api_key():
        return func(os.environ.get('MAGIC_PUBLISHABLE_API_KEY',
                                   'Environment variable MAGIC_PUBLISHABLE_API_KEY is not set.'))

    return inject_magic_publishable_api_key


def did_token_required(func):
    @wraps(func)
    def inject_did_token():
        test_mode = os.getenv('TEST_MODE')
        did_token = ''  # Because even if we're in test-mode, we pass did_token to the render template.
        if test_mode is None or test_mode == 'FALSE':
            try:
                # did_token is the login authorization token from Magic.
                # We're passing the auth token to the form, and back from the form to this route. There's probably a
                # better way to stay logged in, but this works well enough for now.
                if request.method == 'GET':
                    did_token = request.args.get('didt')
                else:
                    did_token = request.form.get('didt')

                magic = Magic(api_secret_key=__get_magic_secret_key())

                # Validate the did_token
                magic.Token.validate(did_token)

                # Sample code: The Magic docs suggest using issuer or public_address as the key for storing and
                # retrieving user data in my app. In this app, we might store/retrieve a user-specific list of piano
                # exercises, for example.
                # issuer = magic.Token.get_issuer(did_token)
                # print('callback: issuer: ' + issuer)
                # public_address = magic.Token.get_public_address(did_token)
                # print('callback: public_address: ' + public_address)

                # Sample code: To get the user's human-readable email address, do this:
                # magic_response = magic.User.get_metadata_by_issuer(issuer)
                # email = magic_response.data['email']
                # print('callback: email: ' + email)

                return func(did_token)
            except Exception as e:
                print('did_token_required: authorization failed: ' + format(e))
                # TODO Consider changing this return statement - it depends on Flask running, which gives us a
                # dependency we don't necessarily want. It's not so bad, because we only invoke authentication within
                # Flask, but it makes it harder to test, if nothing else.
                return redirect(url_for("login"))
        else:
            return func(did_token)

    return inject_did_token
