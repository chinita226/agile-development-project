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
        food = Food(food_name=request.form.get("food_name"),description=request.form.get("description"),quantity=request.form.get("quantity"))
        db.session.add(food)
        db.session.commit()
    food=Food.query.all()
    return render_template('restaurant.html', businessname=current_user.businessname, food=food)
   
# @views.route("/update", methods=["POST"])
# @login_required
# def update():
#         newname = request.form.get("newname")
#         oldname = request.form.get("oldname")
#         newdescription = request.form.get("newdescription")
#         olddescription = request.form.get("olddescription")
#         newquantity = request.form.get("newquantity")
#         oldquantity = request.form.get("oldquantity")
#         food = Food.query.filter_by(food_name=oldname).first()
#         food = Food.query.filter_by(description=olddescription).first()
#         food = Food.query.filter_by(quantity=oldquantity).first()
#         food.food_name = newname
#         food.description = newdescription
#         food.quantity = newquantity
#         db.session.commit()
#         return render_template('restaurant.html')

# @views.route("/delete", methods=["POST"])
# @login_required
# def delete():
#     food_name = request.form.get("food_name")
#     food = Food.query.filter_by(food_name=food_name).delete()
#     db.session.delete(food)
#     db.session.commit()
#     return render_template("restaurant.html")
