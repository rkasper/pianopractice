import os
from functools import wraps

from flask import request, redirect, url_for, session
from magic_admin import Magic


__AUTH_CREDENTIAL_SESSION_KEY = 'magic_credential'


def __get_magic_secret_key():
    return os.environ.get('MAGIC_SECRET_KEY')


def with_magic_publishable_api_key(func):
    @wraps(func)
    def inject_magic_publishable_api_key():
        return func(os.environ.get('MAGIC_PUBLISHABLE_API_KEY',
                                   'Environment variable MAGIC_PUBLISHABLE_API_KEY is not set.'))

    return inject_magic_publishable_api_key


def magic_credential_required(func):
    @wraps(func)
    def inject_did_token():
        test_mode = os.getenv('TEST_MODE')
        print("""session: {}""".format(session))
        magic_credential = session.get('magic_credential')
        print("""magic_credential from the session: {}""".format(magic_credential))
        if test_mode is None or test_mode == 'FALSE':
            try:
                magic_credential = request.args.get('didt')
                print("""from didt: magic_credential is {}""".format(magic_credential))
                if magic_credential is None:
                    magic_credential = request.args.get('magic_credential')
                    print("""from magic_credential: magic_credential is {}""".format(magic_credential))
                    if not magic_credential:
                        magic_credential = session.get(__AUTH_CREDENTIAL_SESSION_KEY)
                        print("""from session: magic_credential is {}""".format(magic_credential))

                # Validate the auth token
                magic = Magic(api_secret_key=__get_magic_secret_key())
                magic.Token.validate(magic_credential)
                print('--- magic_credential is valid ---')
                session[__AUTH_CREDENTIAL_SESSION_KEY] = magic_credential

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

                return func()
            except Exception as e:
                print(e)
                if session.get(__AUTH_CREDENTIAL_SESSION_KEY):
                    session.pop(__AUTH_CREDENTIAL_SESSION_KEY)
                return redirect(url_for("login"))
        else:
            return func()

    return inject_did_token
