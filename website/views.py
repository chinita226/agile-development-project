from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import UserMixin
from flask_login.utils import login_user
from .models import Food
from . import db
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")

@views.route('/<user>')
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        food=Food.query.all()
        return render_template('restaurant.html')
    food=Food.query.all()
    return render_template('npo.html')

# current_user is the object for the logged in user.
@views.route('/<user>', methods=["GET", "POST"])
@login_required
def dashboard1(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant' and request.form:
        food = Food(food_name=request.form.get("food_name"),description=request.form.get("description"),quantity=request.form.get("quantity"))
        db.session.add(food)
        db.session.commit()
        flash("Item added!")
    food=Food.query.all()
    return render_template('restaurant.html', businessname=current_user.businessname, food=food)

@views.route("/update/<int:id>", methods=["POST"])
@login_required
def update(id):
    id = request.form.get("id")
    food = Food.query.get_or_404(id)
    db.session.commit()
    food=Food.query.all()
    flash("Item updated!")
    return redirect(url_for("views.dashboard", user=current_user))

@views.route("/delete", methods=["POST"])
@login_required
def delete():
    id = request.form.get("id")
    food=Food.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Item deleted!")
    food=Food.query.all()
    return redirect(url_for("views.dashboard", user=current_user))