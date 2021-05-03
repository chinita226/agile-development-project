from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user
from flask_login.utils import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Restaurants, Organizations
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    """Signup get request."""
    return render_template('register.html')


@auth.route('/login')
def login():
    """Login get request."""
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    """Login post request, when a user tries to log in."""
    # Retrieve the data the user entered into the form.
    username = request.form.get('username')
    password = request.form.get('password')
    user_type = request.form.get('org_type')

    # Find the user in the database
    if user_type == 'restaurant':
        user = Restaurants.query.filter_by(username=username).first()
    else:
        user = Organizations.query.filter_by(username=username).first()

    # If no user was found or the password was incorrect create error message
    # and redirect to the login page to display it.
    if not user or not check_password_hash(user.password, password):
        flash('Incorrect username or password!', category='error')
        return redirect(url_for('auth.login'))

    # If the above block didnt run, there is a user with the correct
    # credentials. Log the user in and create success message.

    login_user(user)

    flash("Log in Successful!", category='success')

    return redirect(url_for('views.dashboard', user=user.username))


@auth.route('/signup', methods=['POST'])
def signup_post():
    """Signup post request, when a user tries to register."""
    # Retrieve the data the user entered into the form.
    username = request.form.get('username')
    password = request.form.get('password')
    confirm = request.form.get('confirm')
    user_type = request.form.get('org_type')

    # Check if there is a user in the database with the entered username
    if user_type == 'restaurant':
        user = Restaurants.query.filter_by(username=username).first()
    else:
        user = Organizations.query.filter_by(username=username).first()

    # If there is a user, that username is not available
    if user:
        flash('Username not available!', category='error')
    # If no user with entered username, confirm the passwords match.
    elif password != confirm:
        flash('The passwords do not match!', category='error')
    # If username unique and passwords are correct.
    else:
        # Create the new user object from the corresponding model
        if user_type == 'restaurant':
            user = Restaurants(username=username, password=generate_password_hash(password, method='sha256'))
        else:
            user = Organizations(username=username, password=generate_password_hash(password, method='sha256'))

        # Add the user to the database
        db.session.add(user)
        # Save the changes to the database
        db.session.commit()
        # Create message to display to user
        flash('Account created!', category='success')
        # log the user in
        login_user(user)
        # redirect the user to the dashboard
        return redirect(url_for('views.dashboard', user=user.username))

    # If the else block above didn't run, refresh the signup page
    # to display messages to user.
    return redirect(url_for('auth.signup'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


class Auth():
    """Test purpose."""

    def login(self):
        """Test method."""
        print("test")
