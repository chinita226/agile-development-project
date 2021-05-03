from flask import Blueprint, render_template
from flask.helpers import url_for
from flask_login.utils import login_required, current_user
from werkzeug.utils import redirect
from . import db


views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard', user=current_user.username))

    return redirect(url_for('auth.login'))


@views.route('/about')
def about():
    return render_template("about.html")


# current_user is the object for the logged in user.
@views.route('/<user>')
@login_required
def dashboard(user):
    if current_user.user_type == 'restaurant':
        return render_template('restaurant.html')
    elif current_user.user_type == 'organization':
        return render_template('npo.html')
