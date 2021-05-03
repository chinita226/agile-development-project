from flask import Blueprint, render_template, request, flash
from . import db
from flask_login import login_required, current_user
 
views = Blueprint('views', __name__)
 
 
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
