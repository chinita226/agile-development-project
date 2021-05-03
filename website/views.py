from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_login.utils import login_required, current_user
from werkzeug.utils import redirect
from . import db


views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template('index.html')


@views.route('/about')
def about():
    return render_template("about.html")


# current_user is the object for the logged in user.
@views.route('/<user>')
@login_required
def dashboard(user):
    return render_template('dashboard.html', user=current_user.username)
