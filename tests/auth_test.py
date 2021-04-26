import unittest.mock
from website import auth


class TestAuth(unittest.TestCase):

    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def test_login(self, mock_print):
        auth.Auth.login(auth)
        mock_print.assert_called_with("test")

