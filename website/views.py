<<<<<<< HEAD
from flask import Blueprint, render_template, request, flash
=======
from flask import Blueprint, render_template
from flask.helpers import url_for
from flask_login.utils import login_required, current_user
from werkzeug.utils import redirect
>>>>>>> 741512dbe7ca26d0197c05a8612fabf3541b2cf4
from . import db
from flask_login import login_required, current_user
 
views = Blueprint('views', __name__)
<<<<<<< HEAD
 
 
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """Route to home page."""
    return render_template("about.html")
 
@views.route('/npo', methods=['GET', 'POST'])
@login_required
def npo_view():
    attrs = [current_user.user_name, current_user.password]
    for i in attrs:
        print(i)
    return "<h1>It works for NPO</h1>"
=======


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
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        return render_template('restaurant.html')
<<<<<<< HEAD
    elif current_user.user_type == 'organization':
        return render_template('npo.html')
>>>>>>> 741512dbe7ca26d0197c05a8612fabf3541b2cf4
=======
    # Show NPO page
    return render_template('npo.html')
>>>>>>> 7a445a38d4eb6826dec620267b1612219072d2c3
