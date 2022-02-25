import os

from boto.s3.key import Key
from flask import Flask, render_template, request

from Authentication import did_token_required
from pianopractice import PianoPractice
from storage import Storage

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    exercises = PianoPractice.exercises_to_practice()
    print('index: exercises: ' + str(exercises))
    scale = exercises[0]
    print('index: scale: ' + str(scale))
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
@did_token_required
def admin(did_token):
    print('admin:')
    print('admin: did_token: ' + did_token)

    # For this app, all we have to do is validate the token, which we did. Given a valid token, render the
    # auth-protected page.

    bucket = Storage.storage_bucket()
    scales_storage = Key(bucket)
    hanon_storage = Key(bucket)
    blues_storage = Key(bucket)

    if request.method == 'POST':  # The web form supplied the data. Store the new data.
        scales = str(request.form.get(Storage.STORAGE_KEY_SCALES))
        hanon = str(request.form.get(Storage.STORAGE_KEY_HANON))
        blues = str(request.form.get(Storage.STORAGE_KEY_BLUES))

        scales_storage.set_contents_from_string(scales)
        hanon_storage.set_contents_from_string(hanon)
        blues_storage.set_contents_from_string(blues)
    else:  # Get the data from storage.
        scales = Storage.get_scales_as_string()
        hanon = Storage.get_hanon_as_string()
        blues = Storage.get_blues_as_string()

    print('admin: returning render_template')
    return render_template("admin.html",
                           didt=did_token,
                           scales=scales,
                           hanon=hanon,
                           blues=blues)


if __name__ == '__main__':
    app.run()
