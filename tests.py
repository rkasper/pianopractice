import unittest

from test_pianopractice import PianoPracticeTests
from test_storage import StorageTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(PianoPracticeTests())
    suite.addTest(StorageTests())
    return suite


if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
