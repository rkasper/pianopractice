from flask import Flask

from pianopractice import PianoPractice

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    page = '''<!DOCTYPE html><html><head>
<title>PianoPlay.app</title>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7FF50GQ34L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag(''js'', new Date());

  gtag(''config'', ''G-7FF50GQ34L'');
</script>
</head>
<body><h1>PianoPlay</h1>
<p>You can become the pianist you''ve always wanted to be!</p>
<p>Practice your piano exercises just right: the right exercises at the right times; just the right amount of exercise to keep it fun, keep you advancing, and leave you time for the fun stuff on piano&mdash;playing songs and making music!</p>
<h2>Practice these exercises:</h2>
<ul>'''
    for exercise in PianoPractice.exercises_to_practice():
        page += '<li><a href="' + exercise.url + '">' + exercise.group + ': ' + exercise.name + '</a></li>'
    page += '''<li>... and a new exercise</li>
</ul>
<h2>In this sequence of keys:</h2>
<ul><li>'''
    page += '<li>'.join(map(str, PianoPractice.keys_to_practice()))
    page += '''</ul>
<button onClick="window.location.reload();">Randomize!</button>
<br/><br/><br/><a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"><br />PianoPlay.app</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://kasperowski.com/" property="cc:attributionName" rel="cc:attributionURL">Richard Kasperowski</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
</body></html>'''
    return page


if __name__ == '__main__':
    app.run()
