import os
from functools import wraps

from flask import request, redirect, url_for, session
from magic_admin import Magic
from magic_admin.utils.http import parse_authorization_header_value


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
        # print(request.headers.get('X-Auth-TOken'))
        # did_token = parse_authorization_header_value(
        #     request.headers.get('Authorization'),
        # )
        # print('--- Magic''s way: ' + str(did_token))

        test_mode = os.getenv('TEST_MODE')
        print("""session: {}""".format(session))
        magic_credential = session.get('magic_credential')  # Because even if we're in test-mode, we pass did_token to the render template.
        print("""magic_credential from the session: {}""".format(magic_credential))
        if test_mode is None or test_mode == 'FALSE':
            try:
                if not magic_credential:
                    # The login authorization token from Magic is either didt or magic_credential. magic_credential
                    # seems to be the parameter to look for today; didt worked in the past.
                    # We're passing the auth token to the form, and back from the form to this route. There's probably a
                    # better way to stay logged in, but this works well enough for now.
                    magic_credential = request.args.get('didt')
                    print('from didt: did_token is ' + str(magic_credential))
                    if magic_credential is None:
                        magic_credential = request.args.get('magic_credential')
                        print('from magic_credential: magic_credential is ' + str(magic_credential))

                # Validate the auth token
                magic = Magic(api_secret_key=__get_magic_secret_key())
                magic.Token.validate(magic_credential)
                session['magic_credential'] = magic_credential
                print('--- did_token is valid ---')

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
                # Uncomment the following print statement to help debug authentication problems. Otherwise leave it
                # commented-out so test results are easy to read.
                # print('did_token_required: authorization failed: ' + format(e))
                # TODO Consider changing this return statement - it depends on Flask running, which gives us a
                # dependency we don't necessarily want. It's not so bad, because we only invoke authentication within
                # Flask, but it makes it harder to test, if nothing else.
                print(e)
                return redirect(url_for("login"))
        else:
            return func()

    return inject_did_token
