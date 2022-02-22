import json
import os

from boto.s3.key import Key
from flask import Flask, render_template

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


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']

    b = storage_bucket()

    scales = Key(b)
    scales.key = PianoPractice.STORAGE_KEY_SCALES

    hanon = Key(b)
    hanon.key = PianoPractice.STORAGE_KEY_HANON

    blues = Key(b)
    blues.key = PianoPractice.STORAGE_KEY_BLUES

    return """<html><body>
    <script
      src="https://auth.magic.link/pnp/callback"
      data-magic-publishable-api-key=\"""" + magic_publishable_api_key + """"\">
    </script>
    <p>Scales: """ + str(json.dumps(json.loads(scales.get_contents_as_string()))) + """
    <p>Hanon: """ + str(json.loads(hanon.get_contents_as_string())) + """
    <p>Blues School: """ + str(json.loads(blues.get_contents_as_string())) + """
    </body></html>"""


@app.route('/login', methods=['GET'])
def login():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']
    return render_template("login.html",
                           magic_publishable_api_key=magic_publishable_api_key)


@app.route('/callback', methods=['POST', 'GET'])
def callback():
    magic_publishable_api_key = os.environ['MAGIC_PUBLISHABLE_API_KEY']
    return render_template("callback.html",
                           magic_publishable_api_key=magic_publishable_api_key)


if __name__ == '__main__':
    app.run()
