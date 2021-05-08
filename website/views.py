from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import UserMixin
from .models import Food
from . import db
from flask_login import login_required, current_user
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")

# current_user is the object for the logged in user.
@views.route('/<user>', methods = ['POST', 'GET'])
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        return redirect(url_for('views.add'))

@views.route('/add_item', methods=['POST', 'GET'])
@login_required
def add():
    if request.method == 'POST':
        item_name = request.form.get('food_name')
        item_des = request.form.get('description')
        item_quantity = request.form.get('quantity')

        new_item = Food(food_name=item_name, description=item_des, quantity=item_quantity, users_id=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash("Item added!", category='success')

    return render_template("restaurant.html", user=current_user)


@views.route('/delete-food', methods=['POST'])
def delete_food():
    food = json.loads(request.data)
    foodId = food['foodId']
    food = Food.query.get(foodId)
    if food:
        if food.users_id == current_user.id:
            db.session.delete(food)
            db.session.commit()

    return jsonify({})