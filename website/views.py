from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_login.utils import login_required, current_user
from werkzeug.utils import redirect
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


<<<<<<< HEAD
@views.route('/', methods=['GET', 'POST'])
@login_required
=======
@views.route('/')
>>>>>>> e20e89ec37ab91824b8f43c065a80025d5ccf56a
def home():
    """Route to home page."""
    return render_template('index.html')


<<<<<<< HEAD
@views.route('/npo', methods=['GET', 'POST'])
@login_required
def npo_view():
    attrs = [current_user.user_name, current_user.password]
    for i in attrs:
        print(i)
    return "<h1>It works for NPO</h1>"
=======
@views.route('/about')
def about():
    return render_template("about.html")


# current_user is the object for the logged in user.
@views.route('/<user>')
@login_required
def dashboard(user):
    return render_template('dashboard.html', user=current_user.username)
>>>>>>> e20e89ec37ab91824b8f43c065a80025d5ccf56a
