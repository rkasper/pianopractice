from flask import Flask

from pianopractice import PianoPractice

GOOGLE_ANALYTICS = '''<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7FF50GQ34L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-7FF50GQ34L');
</script>'''

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    page = '''<!DOCTYPE html><html><head>
<title>PianoPlay.app</title>

<link href="static/bootstrap-5.1.3-dist/css/bootstrap.min.css" rel="stylesheet">
<link href="static/css/style.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<link rel="shortcut icon" type="image/png" href="static/image/favicon.png"/>
<meta name="viewport" content="width=device-width, initial-scale=1">'''

    page += GOOGLE_ANALYTICS

    page += '''</head>
<body>
    <div class="piano_mb">
        <div class="container-md">
            <div class="row">
                <img class="logo-image" src="static/image/logo.png">
            </div>
                <div class="row piano_mb_tex-col">
                <div class="col-md-7">
                    <h1>Piano Play</h1>
                    <p class="piano_mb_title1">You can become the pianist you've always <span style="color: #95AB68">wanted to be!</span></p>
                    <p class="piano_mb-regular-text">Practice your piano exercises just right: the right exercises at the right times; just the right amount of exercise to keep it fun, keep you advancing, and leave you time for the fun stuff on piano&mdash;playing songs and making music!</p>
                </div>
                <div class="container-fluid d-lg-none d-md-none piano-race-img-mobile">
                    <img src="static/image/piano-img.jpg" class="img-fluid">
                </div>
            </div>
        </div>
    </div>
    <div class="piano_exercises">
        <div class="container-md">
            <div class="row">
                <h2 class="title-h2">Practice <span style="color: #95AB68">these exercises:</span></h2>
            </div>
        </div>
        <div class="container-md d-flex exercises-row">
            <ul class="d-flex exercises-row1">'''

    exercises = PianoPractice.exercises_to_practice()
    page += '<li class="d-flex flex-column"><a href="' + exercises[
        0].url + '" target="_blank"><img src="static/image/exercise-img1.png">' + exercises[0].group + ': ' + exercises[
                0].name + '</a></li>'
    page += '<li class="d-flex flex-column"><a href="' + exercises[
        1].url + '" target="_blank"><img src="static/image/exercise-img2.png">' + exercises[1].group + ': ' + exercises[
                1].name + '</a></li>'
    page += '<li class="d-flex flex-column"><a href="' + exercises[
        2].url + '" target="_blank"><img src="static/image/exercise-img3.png">' + exercises[2].group + ': ' + exercises[
                2].name + '</a></li>'

    page += '''<li class="d-flex flex-column"><img src="static/image/exercise-img4.png">... and a new exercise</li>
            </ul>
        </div>
    </div>
    <div class="piano_keys">
        <div class="container-fluid">
            <div class="container-md">
                <h2>In this <span style="color: #fff;">sequence of keys:</span></h2>
                </div>
            <ul class="d-flex piano_keys-cols">'''

    for key in PianoPractice.keys_to_practice():
        page += '<li class="d-flex piano_keys-cols">' + key

    page += '''</ul>
            </div>
    </div>
    <div class="piano_randomize-btn">
        <button class="randomize-btn" onClick="window.location.reload();">Randomize!</button>
    </div>
    <div class="footer container-md">
        <div class="footer-img">
            <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
        </div>
        <div class="footer-text">
        <span xmlns:dct="https://purl.org/dc/terms/" property="dct:title">PianoPlay.app</span> by <a xmlns:cc="https://creativecommons.org/ns#" href="https://kasperowski.com/" property="cc:attributionName" rel="cc:attributionURL" target="_blank">Richard Kasperowski</a> is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
        </div>
    </div>

    <script src="static/bootstrap-5.1.3-dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

    return page


if __name__ == '__main__':
    app.run()
