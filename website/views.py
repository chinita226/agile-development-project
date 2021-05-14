from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.globals import session
from .models import Food, User
from . import db
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")

@views.route('/food-waste')
def blog():
    return render_template("blog.html")

@views.route('/<user>', methods=["POST", "GET"])
@login_required
def dashboard(user):
    # Show restaurant page
    if current_user.user_type == 'restaurant':
        if request.form:
            food = Food(
            food_name=request.form.get("food_name"),
            description=request.form.get("description"),
            quantity=request.form.get("quantity"),
            users_id=current_user.id
            )

            db.session.add(food)
            db.session.commit()
            flash("Item added!")

        food=Food.query.filter_by(users_id=current_user.id).all()
        return render_template('restaurant.html', businessname=current_user.businessname, food=food)

    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    search = False

    q = request.args.get('q')
    if q:
        search = True
    if request.method == 'POST' and 'tag' in request.form:
        tag = request.form["tag"]
        if not tag:
            flash("Missing keyword")
            return redirect(url_for("views.dashboard", user=current_user))
        search = "%{}%".format(tag)
        locations = User.query.filter(User.location.like(search)).order_by(User.location)
        location=locations.limit(per_page).offset(offset)
        if location == []:
            flash("not found")
            return render_template('npo.html', businessname=current_user.businessname, food =[], tag=tag)
        for i in location:
            foods= Food.query.filter_by(users_id=i.id).order_by(Food.food_name)
        food= foods.limit(per_page).offset(offset)
        pagination= Pagination(page=page,per_page=per_page,offset=offset, total=foods.count(),css_framework='bootstrap3', 
                           search=search)
        return render_template('npo.html', businessname=current_user.businessname, food=food, users=location, tag=tag,
        pagination=pagination)

    food = Food.query.order_by(Food.food_name)
    users = User.query.order_by(User.id)
    food_for_render = food.limit(per_page).offset(offset)
    users_for_render = users.limit(per_page).offset(offset)

    pagination = Pagination(page=page, per_page=per_page, offset=offset,
                           total=food.count(), css_framework='bootstrap3', 
                           search=search)
    # Show NPO page
    return render_template('npo.html',
                           businessname=current_user.businessname,
                           food=food_for_render,
                           users=users_for_render, pagination=pagination)





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