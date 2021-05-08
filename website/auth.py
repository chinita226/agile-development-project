from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
# from .views import update
from .models import User
from .models import Food
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

 
@auth.route('/signup')
def signup():
    """Signup get request."""
    return render_template('signup.html')
 
 
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
    user = User.query.filter_by(username=username).first()
 
    # If no user was found or the password was incorrect create error message
    # and redirect to the login page to display it.
    if not user:
        flash("Incorrect username!", category='error')
        return redirect(url_for('auth.login'))
    elif not check_password_hash(user.password, password):
        flash('Incorrect password!', category='error')
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
    password = request.form.get('password1')
    confirm = request.form.get('password2')
    businessname = request.form.get('businessname')
    location = request.form.get('location')
    user_type = request.form.get('org_type')


    # Check if there is a user in the database with the entered username
    user = User.query.filter_by(username=username).first()
    user_business = User.query.filter_by(businessname=businessname).first()
    # If there is a user, that username is not available. Create error msg
    if user:
        flash('Username not available!', category='error')
    elif user_business:
        flash('Business name is already in use!', category='error')
    # If no user with entered username, confirm the passwords match. If they
    # don't match, create the error message.
    elif password != confirm:
        flash('The passwords do not match!', category='error')
    # If username unique and passwords are correct.
    else:
        # Create the new user object
        user = User(username=username,
                    password=generate_password_hash(password, method='sha256'),
                    user_type=user_type,
                    businessname=businessname,
                    location=location)
 
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

 
@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
 
# @auth.route('/restaurant', method=['POST'])
# def updating():
#     food_name =request.form.get('food_name')

#     food = Food(id = id,
#                 food_name = food_name,
#                 description = description,
#                 quantity= quantity,
#                 users_id = users_id)
#     db.session.add(food)
#     update(food)
#     return redirect(url_for('views.update', food=food))