# Piano Practice
_Simple guidance for piano practice_

Simply answers these important questions:
- What exercises should I practice right now?
- In what sequence of keys should I practice them?

## Dev & test notes
- To run unit tests: 

`$ venv/bin/python pianopractice/test/tests.py`

## Environment variables
We use a number of environment variables to configure the server. It's OK to stare secrets in environments variables - just make sure you don't commit any of them to the repository.
- `CELLAR_ADDON_HOST=some.host.name`: Specifies the hostname of our S3 external storage. In production, DigitalOcean injects this for us automatically.
- `CELLAR_ADDON_KEY_ID=RandomLookingString`: Specifies our S3 key. In production, DigitalOcean injects this for us automatically.
- `CELLAR_ADDON_KEY_SECRET=RandomLookingString`: Specifies our S3 secret key. In production, DigitalOcean injects this for us automatically.
- `MAGIC_PUBLISHABLE_API_KEY=pk_live_RandomLookingString`: Specifies the publishable API key for Magic, our authentication provider
- `MAGIC_SECRET_KEY=sk_live_RandomLookingString`: Specifies the secret key for Magic, our authentication provider
- `MOCK_DB=true`: If this environment variable exists, use a fake in-memory database. *Do not set in production.*
- `TEST_MODE=TRUE`: If this environment variable exists, we can access protected web pages *without* authenticating. *Do not set in production.*

## Deployment notes
- Try deploying to clever-cloud.com. It's pretty wicked easy.
- For that to work, you'll have to create a `requirements.txt` file full of package dependencies. To create
`requirements.txt`:

`$ pip freeze > requirements.txt`

To run the production server:

`$ gunicorn --worker-tmp-dir /dev/shm --config gunicorn_config.py flask-app:app`

That is all. Enjoy!