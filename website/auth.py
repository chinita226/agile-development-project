from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Route to restaurants users, return login template."""
    if request.method == 'POST':
        userName = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('org_type')

        user = User.query.filter_by(user_name=userName).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Log in successfully", category='success')
                login_user(user, remember=True)
                if user_type == 'restaurant':
                    return redirect(url_for('views.home'))
                return redirect(url_for('views.npo_view'))

    return render_template("login.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(user_name=username).first()
        if user:
            flash('A restaurant user with same name already exists.', category='error')
        elif password1 != password2:
            flash('Password must be the same.', category='error')
        else:
            new_user = User(user_name=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

class Auth():
    """Test purpose."""

    def login(self):
        """Test method."""
        print("test")

