import json
import os

from boto.s3.key import Key
from flask import Flask, render_template, request, redirect, url_for
from magic_admin import Magic
from magic_admin.utils.http import parse_authorization_header_value
from magic_admin.error import DIDTokenError
from werkzeug.exceptions import BadRequest

from pianopractice import PianoPractice, storage_bucket

GOOGLE_ANALYTICS = '''<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7FF50GQ34L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-7FF50GQ34L');
</script>'''

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    exercises = PianoPractice.exercises_to_practice()
    scale = exercises[0]
    hanon = exercises[1]
    blues = exercises[2]
    keys = PianoPractice.keys_to_practice()
    return render_template("index.html",
                           scale_name=scale[PianoPractice.NAME], scale_url=scale[PianoPractice.URL],
                           hanon_name=hanon[PianoPractice.NAME], hanon_url=hanon[PianoPractice.URL],
                           blues_name=blues[PianoPractice.NAME], blues_url=blues[PianoPractice.URL],
                           keys=keys)


@app.route('/admin', methods=['GET'])
def admin():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']

    print('admin: request.authorization: ' + request.authorization)
    print('admin: request.headers: ' + str(request.headers))
    authorization_header = request.headers.get('Authorization')
    if authorization_header: # Maybe the user tried logging in. Let's see if they authenticated.
        print("admin: Validating authorization.")
        did_token = parse_authorization_header_value(
            request.headers.get('Authorization'),
        )
        if did_token is None:
            raise BadRequest(
                'Authorization header is missing or header value is invalid',
            )

        magic = Magic()

        # Validate the did_token
        try:
            magic.Token.validate(did_token)
            issuer = magic.Token.get_issuer(did_token)
        except DIDTokenError as e:
            raise BadRequest('DID Token is invalid: {}'.format(e))

        # # Use your application logic to load the user info.
        # user_info = logic.User.load_by(issuer=issuer)

        b = storage_bucket()

        scales = Key(b)
        scales.key = PianoPractice.STORAGE_KEY_SCALES

        hanon = Key(b)
        hanon.key = PianoPractice.STORAGE_KEY_HANON

        blues = Key(b)
        blues.key = PianoPractice.STORAGE_KEY_BLUES

        return render_template("admin.html",
                               magic_publishable_api_key=magic_publishable_api_key,
                               scales=str(json.dumps(json.loads(scales.get_contents_as_string()))),
                               hanon=str(json.loads(hanon.get_contents_as_string())),
                               blues=str(json.loads(blues.get_contents_as_string())))

    else: # We got here without trying to log in. Redirect to the /login page.
        print("admin: Attempted to GET /admin, but there's no Authentication header. Redirecting to login.")
        return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def login():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']
    return render_template("login.html",
                           magic_publishable_api_key=magic_publishable_api_key)


@app.route('/callback', methods=['GET'])
def admin():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']

    print('callback: request.authorization: ' + request.authorization)
    print('callback: request.headers: ' + str(request.headers))
    authorization_header = request.headers.get('Authorization')
    if authorization_header: # Maybe the user tried logging in. Let's see if they authenticated.
        print("callback: Validating authorization.")
        did_token = parse_authorization_header_value(
            request.headers.get('Authorization'),
        )
        if did_token is None:
            raise BadRequest(
                'Authorization header is missing or header value is invalid',
            )

        magic = Magic()

        # Validate the did_token
        try:
            magic.Token.validate(did_token)
            issuer = magic.Token.get_issuer(did_token)
        except DIDTokenError as e:
            raise BadRequest('DID Token is invalid: {}'.format(e))

    return render_template("callback.html",
                           magic_publishable_api_key=magic_publishable_api_key)

if __name__ == '__main__':
    app.run()
