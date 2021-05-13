from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from . import db
from .models import Food

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")


@views.route('/insight')
def insight():
    """Route to insight page."""
    return render_template("insight.html")


@views.route('/food-waste')
def blog():
    return render_template("blog.html")


@views.route('/<user>')
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        food = Food.query.filter_by(users_id=current_user.id).all()
        return render_template('restaurant.html', businessname=current_user.businessname, food=food)
    
    food = Food.query.all()
    # Show NPO page
    return render_template('npo.html', businessname=current_user.businessname, food=food)


# current_user is the object for the logged in user.
@views.route('/<user>', methods=["POST"])
@login_required
def add(user):
    # Show and add items in restaurant page
    if current_user.user_type == 'restaurant' and request.form:
        food = Food(
            food_name=request.form.get("food_name"),
            description=request.form.get("description"),
            quantity=request.form.get("quantity"),
            users_id=current_user.id
        )
        
        db.session.add(food)
        db.session.commit()
        flash("Item added!")
    
    food = Food.query.filter_by(users_id=current_user.id).all()
    return render_template('restaurant.html', businessname=current_user.businessname, food=food)


# Changed the code
@views.route("/update", methods=["POST"])
@login_required
def update():
    # Show and Update items in restaurant page
    _id = request.form.get("id")
    name = request.form.get("name")
    des = request.form.get("des")
    quantity = request.form.get("quantity")
    food = Food.query.filter_by(id=_id).first()
    food.food_name = name
    food.description = des
    food.quantity = quantity
    db.session.commit()
    return redirect(url_for("views.dashboard", user=current_user))


@views.route("/delete", methods=["POST"])
@login_required
def delete():
    # Show and delete items in restaurant page
    id = request.form.get("id")
    Food.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Item deleted!")
    Food.query.all()
    return redirect(url_for("views.dashboard", user=current_user))
