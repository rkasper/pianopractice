from flask import Flask

from pianopractice import PianoPractice

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    page = '<!DOCTYPE html><html><head><title>Piano Practice</title></head><body><h1>Yay Piano Exercises!</h1>'
    page += '<h2>Practice these exercises:</h2>'
    page += '<ul>'
    for exercise in PianoPractice.exercises_to_practice():
        page += '<li><a href="' + exercise.url + '">' + exercise.group + ': ' + exercise.name + '</a></li>'
    page += '</ul>'
    page += '<h2>Practice the 12 keys in this sequence:</h2>'
    page += '<ul><li>'
    page += '<li>'.join(map(str, PianoPractice.keys_to_practice()))
    page += '</ul></body></html>'
    return page


if __name__ == '__main__':
    app.run()
