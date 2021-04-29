from flask import Blueprint, render_template, request, flash, redirect, url_for
import sqlite3



auth = Blueprint('auth', __name__)


@auth.route('/restaurants', methods=['GET', 'POST'])
def login_restaurants():
    """Route to restaurants users, return login template."""
    
    if request.method == 'POST':
        username_val = request.form.get('userName')
        password_val = request.form.get('password')
        connection = sqlite3.connect('../database.db')
        cur = connection.cursor()
        cur.execute("SELECT password FROM restaurants WHERE userName=?", (username_val,))
        row = cur.fetchone()
        connection.commit()
        if password_val == row:
            flash("Log in successfully", category='success')

    return render_template("login.html")


@auth.route('/npo', methods=['GET', 'POST'])
def login_npos():
    """Route to non-profit users, return login template."""
    if request.method == 'POST':
        username_val = request.form.get('userName')
        password_val = request.form.get('password')
        connection = sqlite3.connect('../database.db')
        cur = connection.cursor()
        cur.execute("SELECT password FROM organizations WHERE userName=?", (username_val,))
        row = cur.fetchone()
        connection.commit()
        if password_val == row:
            flash("Log in successfully", category='success')

    return render_template("login.html")



class Auth():
    """Test purpose."""

    def login(self):
        """Test method."""
        print("test")
