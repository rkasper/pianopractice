import unittest

from test_authentication import AuthenticationTests
from test_pianopractice import PianoPracticeTests
from test_storage import StorageTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(PianoPracticeTests())
    suite.addTest(StorageTests())
    suite.addTest(AuthenticationTests())
    return suite


if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
