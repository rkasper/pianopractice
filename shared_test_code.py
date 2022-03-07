import warnings


def ignore_warnings(test_method):
    def test_run(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            test_method(self, *args, **kwargs)

    return test_run
