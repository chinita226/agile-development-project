from flask import Blueprint, render_template, request, flash
from flask_login import UserMixin
from .models import Food
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")

# current_user is the object for the logged in user.
@views.route('/<user>', methods=["GET", "POST"])
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant' and request.form:
        food = Food(food_name=request.form.get("food_name"))
        db.session.add(food)
        db.session.commit()
    food=Food.query.all()
    return render_template('restaurant.html', businessname=current_user.businessname, food=food)
    

    # Show NPO page
#return render_template('npo.html', businessname=current_user.businessname)