# Piano Practice
_Simple guidance for piano practice_

Simply answers these important questions:
- What exercises should I practice right now?
- In what sequence of keys should I practice them?

## Deployment notes
- Try deploying to clever-cloud.com. It's pretty wicked easy.
- For that to work, you'll have to create a `requirements.txt` file full of package dependencies. To create
`requirements.txt`:

`# pip freeze > requirements.txt`

- And you'll have to set an environment variable to tell clever-cloud.com where to find the Flask app. In our case, it
will look like this:

`CC_PYTHON_MODULE="app:app"`

- If we renamed app.py to something else, then we'd do this instead:

`CC_PYTHON_MODULE="newfilename:app"`

That is all. Enjoy!