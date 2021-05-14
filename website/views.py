from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.globals import session
from .models import Food, User
from . import db
from flask_login import login_required, current_user
from flask_paginate import Pagination

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")


@views.route('/food-waste')
def blog():
    return render_template("blog.html")


@views.route('/<user>')
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant':

        food = Food.query.filter_by(users_id=current_user.id).all()

        return render_template(
            'restaurant.html',
            businessname=current_user.businessname,
            food=food)

    food = Food.query.order_by(Food.food_name)
    users = User.query.all()

    # Show NPO page
    return render_template('npo.html',
                           businessname=current_user.businessname,
                           food=food,
                           users=users)


@views.route('/search', methods=["POST"])
@login_required
def npo_search():

    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    search = False

    q = request.args.get('q')

    if q:
        search = True

    if 'tag' in request.form:
        tag = request.form["tag"]

        search = "%{}%".format(tag)
        location = User.query.filter(User.location.like(search)).order_by(User.location)
        location_for_render = location.limit(per_page).offset(offset)

        # if location == []:
        #     flash("not found")
        #     return render_template('npo.html', businessname=current_user.businessname, food =[], tag=tag)
        """
        What if a user searches by restaurant name and not location? You
        will need to query the database for that too and have another variable
        that holds the return value for that the same as you have for location.
        Then you will need to check using if statements if there is a value for
        location or businessname etc.
        Also if no results were found for the search term, you will need to handle that
        also.
        """
        for i in location:
            food = Food.query.filter_by(users_id=i.id).order_by(Food.food_name)
            food_for_render = food.limit(per_page).offset(offset)

        pagination = Pagination(
            page=page,
            per_page=per_page,
            offset=offset,
            total=food.count(),
            css_framework='bootstrap3',
            search=search)

        return render_template(
            'npo.html',
            businessname=current_user.businessname,
            food=food_for_render,
            users=location_for_render,
            tag=tag,
            pagination=pagination)

    food = Food.query.order_by(Food.food_name)
    users = User.query.order_by(User.id)
    food_for_render = food.limit(per_page).offset(offset)
    users_for_render = users.limit(per_page).offset(offset)

    pagination = Pagination(page=page,
                            per_page=per_page,
                            offset=offset,
                            total=food.count(),
                            css_framework='bootstrap3',
                            search=search)

    return render_template('npo.html',
                           businessname=current_user.businessname,
                           food=food_for_render,
                           users=users_for_render, pagination=pagination)



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



@views.route("/update/<id>", methods=["POST"])
@login_required
def update(id):
    id = request.form.get('id')
    name = request.form.get('name')
    description = request.form.get('description')
    quantity = request.form.get('quantity')

    food = Food.query.filter_by(id=id).first()

    food.food_name = name
    food.description = description
    food.quantity = quantity

    db.session.commit()
    flash('Item Updated!')

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