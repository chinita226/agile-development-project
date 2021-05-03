import unittest.mock
import views
from website import views
from website import auth
import website


class TestAuth(unittest.TestCase):

    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def home(self, mock_print):
        views.View.home(views)
        mock_print.assert_called_with("test")
        
    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def dashboard(self, mock_print):
        views.View.dashboard(views)
        mock_print.assert_called_with("test")
        
    @unittest.mock.patch("builtins.print", autospec=True, side_effect=print)
    def about(self, mock_print):
        views.View.about(views)
        mock_print.assert_called_with("test")
        