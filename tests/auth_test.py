import unittest.mock
import views
from website import auth


class TestAuth(unittest.TestCase):

    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def about(self, mock_print):
        views.View.about(views)
        mock_print.assert_called_with("test")

def test_register(self):
    rv = self.create_user('John','Smith','John.Smith@myschool.edu', 'helloworld')
    self.assertEquals(rv.status, "200 OK")
    # self.assert_redirects(rv, url_for('splash.dashboard'))