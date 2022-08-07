import os

from flask import Flask, render_template, request
from magic_admin import Magic

from app.authentication import did_token_required, with_magic_publishable_api_key, __get_magic_secret_key
from app.pianopractice import PianoPractice
from app.storage import Storage

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
@with_magic_publishable_api_key
def login(magic_publishable_api_key):
    return render_template("login.html",
                           magic_publishable_api_key=magic_publishable_api_key)


@app.route('/admin', methods=['GET', 'POST'])
#@did_token_required
#def admin(did_token):
@with_magic_publishable_api_key
def admin(magic_publishable_api_key):
    print('admin')

    # TODO Simplify this:
    # - Get the did_token, create the Magic instance, validate the did_token.
    # - If the did_token is valid, return render_template("admin.html")
    # - Else return render_template("login.html")
    try:
        # did_token is the login authorization token from Magic.
        # We're passing the auth token to the form, and back from the form to this route. There's probably a
        # better way to stay logged in, but this works well enough for now.
        if request.method == 'GET':
            print('GET')
            did_token = request.args.get('didt')
            print('from didt: did_token is ' + str(did_token))
            if (did_token == None):
                did_token = request.args.get('magic_credential')
            print('from magic_credential: did_token is ' + str(did_token))
        else:
            print('POST')
            did_token = request.form.get('didt')
            print('from didt: did_token is ' + str(did_token))
            if (did_token == None):
                did_token = request.args.get('magic_credential')
            print('from magic_credential: did_token is ' + str(did_token))

        # Validate the did_token
        magic = Magic(api_secret_key=__get_magic_secret_key())
        magic.Token.validate(did_token)
        print('--- did_token is valid ---')

        # DID token is valid - go ahead and render the admin page
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
                               # didt=did_token,
                               magic_publishable_api_key=magic_publishable_api_key,
                               scales=scales,
                               hanon=hanon,
                               blues=blues)

    except Exception as e:
        # DID token is invalid. Login.
        #return redirect(url_for("login"))
        print(e)
        print('--- did_token is invalid ---')
        return render_template("login.html",
                               magic_publishable_api_key=magic_publishable_api_key)




if __name__ == '__main__':
    app.run()
