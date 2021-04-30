from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Restaurants, Orgazations, Food
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Route to restaurants users, return login template."""
    if request.method == 'POST':
        username = request.form.get('userName')
        password = request.form.get('password')
        user_type = request.form.get('org_type')

        if user_type == 'restaurant':
            user = Restaurants.query.filter_by(user_name=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Log in for restaurant user successfully", category='success')
                    return redirect(url_for('views.home'))
        else:
            user = Orgazations.query.filter_by(user_name=username).first()
            if user:
                if check_password_hash(user.password, password):
                    flash("Log in for npo successfully", category='success')
                    return redirect(url_for('views.home'))
    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user_type = request.form.get('org_type')

        if user_type == 'restaurant':
            user = Restaurants.query.filter_by(user_name=username).first()
            if user:
                flash('A restaurant user with same name already exists.', category='error')
            elif password1 != password2:
                flash('Password must be the same.', category='error')
            else:
                new_user = Restaurants(user_name=username, password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Restaurant account created!', category='success')
                return redirect(url_for('views.home'))
        else:
            user = Orgazations.query.filter_by(user_name=username).first()
            if user:
                flash('An organization with the same user name already exists.', category='error')
            elif password1 != password2:
                flash('Password must be the same.', category='error')
            else:
                new_user = Orgazations(user_name=username, password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('An NPO account created!', category='success')
                return redirect(url_for('views.home'))
    return render_template("test.html")


class Auth():
    """Test purpose."""

    def login(self):
        """Test method."""
        print("test")
