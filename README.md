# Piano Practice
_Simple guidance for piano practice_

Simply answers these important questions:
- What exercises should I practice right now?
- In what sequence of keys should I practice them?

## Environment variables
- `CELLAR_ADDON_HOST=some.host.name`: Specifies the hostname of our S3 external storage. In production, Clever Cloud injects this for us automatically.
- `CELLAR_ADDON_KEY_ID=RandomLookingString`: Specifies the Clever Cloud addon key ID for Cellar, Clever Cloud's S3 clone. In production, Clever Cloud injects this for us automatically.
- `CELLAR_ADDON_KEY_SECRET=RandomLookingString`: Specifies the Clever Cloud addon key secret for Cellar, Clever Cloud's S3 clone. In production, Clever Cloud injects this for us automatically.
- `MAGIC_PUBLISHABLE_API_KEY=pk_live_RandomLookingString`: Specifies the publishable API key for Magic, our authentication provider
- `MAGIC_SECRET_KEY=sk_live_RandomLookingString`: Specifies the secret key for Magic, our authentication provider
- `MOCK_DB=true`: If this environment variable exists, use a fake in-memory database.
- `TEST_MODE=TRUE`: If this environment variable exists, we can access protected web pages *without* authenticating.

## Deployment notes
- Try deploying to clever-cloud.com. It's pretty wicked easy.
- For that to work, you'll have to create a `requirements.txt` file full of package dependencies. To create
`requirements.txt`:

`# pip freeze > requirements.txt`

- And you'll have to set an environment variable to tell clever-cloud.com where to find the Flask app. In our case, it
will look like this:

`CC_PYTHON_MODULE="flask-app:app"`

- And we like to run tests in the deployment environment. In clever-cloud.com, we do this to run tests:

`CC_POST_BUILD_HOOK="python tests.py"`

That is all. Enjoy!