import os

from flask import Flask, render_template, request

from pianopractice.authentication import magic_credential_required, with_magic_publishable_api_key
from pianopractice.pianopractice import PianoPractice
from pianopractice.storage import Storage

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')


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
@with_magic_publishable_api_key
def login(magic_publishable_api_key):
    return render_template("login.html",
                           magic_publishable_api_key=magic_publishable_api_key)


@app.route('/admin', methods=['GET', 'POST'])
@magic_credential_required
def admin():
    print('admin')
    if request.method == 'POST':  # The web form supplied the data. Store the new data.
        scales = str(request.form.get(Storage.STORAGE_KEY_SCALES))
        hanon = str(request.form.get(Storage.STORAGE_KEY_HANON))
        blues = str(request.form.get(Storage.STORAGE_KEY_BLUES))

        Storage.set_scales_from_string(scales)
        Storage.set_hanon_from_string(hanon)
        Storage.set_blues_from_string(blues)
    else:  # Get the data from storage.
        scales = Storage.get_scales_as_string()
        hanon = Storage.get_hanon_as_string()
        blues = Storage.get_blues_as_string()

    return render_template("admin.html",
                           scales=scales,
                           hanon=hanon,
                           blues=blues)


if __name__ == '__main__':
    app.run()
