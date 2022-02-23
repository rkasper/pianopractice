import json
import os

from boto.s3.key import Key
from flask import Flask, render_template, request, redirect, url_for
from magic_admin import Magic

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


@app.route('/login', methods=['GET'])
def login():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']
    return render_template("login.html",
                           magic_publishable_api_key=magic_publishable_api_key)


# TODO Method too long
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    test_mode = os.getenv('TEST_MODE')
    did_token = ''  # Because even if we're in test-mode, we pass did_token to the render template.
    if test_mode is None or test_mode == 'FALSE':
        try:
            # This is the login authorization token from Magic.
            did_token = request.args.get('didt')

            magic_secret_key = os.environ['MAGIC_SECRET_KEY']
            magic = Magic(api_secret_key=magic_secret_key)

            # Validate the did_token
            magic.Token.validate(did_token)
            print('callback: validated did_token')

            # Sample code: The Magic docs suggest using issuer or public_address as the key for storing and retrieving
            # user data in my app. In this app, we might store/retrieve a user-specific list of piano exercises, for
            # example.
            # issuer = magic.Token.get_issuer(did_token)
            # print('callback: issuer: ' + issuer)
            # public_address = magic.Token.get_public_address(did_token)
            # print('callback: public_address: ' + public_address)

            # Sample code: To get the user's human-readable email address, do this:
            # magic_response = magic.User.get_metadata_by_issuer(issuer)
            # email = magic_response.data['email']
            # print('callback: email: ' + email)
        except Exception as e:
            print('Authorization failed: ' + format(e))
            return redirect(url_for("login"))

    # For this app, all we have to do is validate the token, which we did. Given a valid token, render the
    # auth-protected page.

    # TODO Is this necessary? Maybe we don't have to declare these outside of the if-then statement.
    scales = ''
    hanon = ''
    blues = ''

    # TODO flask-app shouldn't have to know anything about S3 storage. Encapsulate it elsewhere.

    b = storage_bucket()

    scales_storage = Key(b)
    scales_storage.key = PianoPractice.STORAGE_KEY_SCALES

    hanon_storage = Key(b)
    hanon_storage.key = PianoPractice.STORAGE_KEY_HANON

    blues_storage = Key(b)
    blues_storage.key = PianoPractice.STORAGE_KEY_BLUES

    if request.method == 'POST':  # The web form supplied the data. Store the new data.
        scales = str(request.form.get(PianoPractice.STORAGE_KEY_SCALES))
        hanon = str(request.form.get(PianoPractice.STORAGE_KEY_HANON))
        blues = str(request.form.get(PianoPractice.STORAGE_KEY_BLUES))

        scales_storage.set_contents_from_string(scales)
        hanon_storage.set_contents_from_string(hanon)
        blues_storage.set_contents_from_string(blues)
    else:  # Get the data from storage.
        # json.dumps(json.loads(...)) seems redundant, but it's not. It's a hack that converts the stored data from a
        # b'...' kind of string to a plain-old string. I bet there's a better way, but this is adequate for now.
        scales = str(json.dumps(json.loads(scales_storage.get_contents_as_string())))
        hanon = str(json.dumps(json.loads(hanon_storage.get_contents_as_string())))
        blues = str(json.dumps(json.loads(blues_storage.get_contents_as_string())))

    return render_template("admin.html",
                           dtdt=did_token,
                           scales=scales,
                           hanon=hanon,
                           blues=blues)


if __name__ == '__main__':
    app.run()
