from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET', 'POST'])
def home():
    """Route to home page."""
    return render_template("login.html")

@auth.route('/restaurants', methods=['GET', 'POST'])
def login_restaurants():
    """Route to restaurants users, return login template."""
    return render_template("login.html")

@auth.route('/npo', methods=['GET', 'POST'])
def login_npos():
    """Route to non-profit users, return login template."""
    return render_template("login.html")











class Auth():
    """Test purpose."""

    def login(self):
        """Test method."""
        print("test")
