import unittest

from website import create_test_app


class BaseTestCase(unittest.TestCase):

    app = create_test_app()
