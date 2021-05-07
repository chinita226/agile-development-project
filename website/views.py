from flask import Blueprint, render_template, request, flash
from flask_login import UserMixin
from models import Food
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")

# current_user is the object for the logged in user.
@views.route('/<user>')
@login_required
def dashboard(user):
    food = Food(title=request.form.get("food"))
    db.session.add(food)
    db.session.commit()
    foods = Food.query.all()
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        return render_template('restaurant.html', businessname=current_user.businessname,foods=foods)
    # Show NPO page
    return render_template('npo.html', businessname=current_user.businessname,foods=foods)
