from flask_testing import TestCase
import unittest.mock
from website import __init__
import unittest
    
class BaseTestCase(TestCase):
    def create_app(self):
        return create_app('test')
    
class Testinit(unittest.TestCase):

    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def test_create_table(self, mock_print):
        __init__.Init.create_table(__init__)
        mock_print.assert_called_with("Created Database!")

