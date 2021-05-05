from flask import Blueprint, render_template, redirect, url_for
from . import db
from flask_login import login_required, current_user
 
views = Blueprint('views', __name__)
 
 
@views.route('/')
def home():
    """Route to home page."""
<<<<<<< HEAD
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard', user=current_user.username))
 
    return redirect(url_for('auth.login'))
 
 
@views.route('/about')
def about():
    return render_template("about.html")
 
 
=======
    return render_template("about.html")

>>>>>>> a9d16e18ee39a33b6919e3608fedd74c8349f54f
# current_user is the object for the logged in user.
@views.route('/<user>')
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        return render_template('restaurant.html')
    # Show NPO page
    return render_template('npo.html')