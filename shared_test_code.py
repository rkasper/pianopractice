import warnings


# The boto S3 storage API doesn't close socket connections. This is intentional, and it's OK. But the unittest runner
# emits warning messages about this, which makes it harder to read test results. Wrap tests in @ignore_warnings to
# silence the warnings and make test results easier to read. Be careful with this. ;-)
# I borrowed this code from
# https://www.alanwsmith.com/posts/20eops3yw16k--suppress-python-mysql-connector-deprecationwarning-and-resourcewarnings-in-unittests
# Thanks, friend!
def ignore_warnings(test_method):
    def test_run(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            test_method(self, *args, **kwargs)

    return test_run
