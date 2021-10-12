from flask import Flask

from pianopractice import PianoPractice

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    page = '<!DOCTYPE html><html><head><title>PianoPlay.app</title></head>'
    page += '<body><h1>PianoPlay</h1>'
    page += '<p>You can become the pianist you''ve always wanted to be!</p>'
    page += '<p>Practice your piano exercises just right: the right exercises at the right times; just the right amount of exercise to keep it fun, keep you advancing, and leave you time for the fun stuff on piano&mdash;playing songs and making music!</p>'
    page += '<h2>Practice these exercises:</h2>'
    page += '<ul>'
    for exercise in PianoPractice.exercises_to_practice():
        page += '<li><a href="' + exercise.url + '">' + exercise.group + ': ' + exercise.name + '</a></li>'
    page += '<li>... and a new exercise</li>'
    page += '</ul>'
    page += '<h2>In this sequence of keys:</h2>'
    page += '<ul><li>'
    page += '<li>'.join(map(str, PianoPractice.keys_to_practice()))
    page += '</ul></body></html>'
    return page


if __name__ == '__main__':
    app.run()
