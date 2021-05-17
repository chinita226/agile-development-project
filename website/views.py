from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Food, User
from . import db
from flask_login import login_required, current_user


views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    return render_template("about.html")


@views.route('/insight')
@login_required
def insight():
    """Route to insight page."""
    if current_user.user_type == 'restaurant':
        food = Food.query.filter_by(users_id=current_user.id).all()
        names, values = [], []
        for item in food:
            names.append(item.food_name)
            values.append(item.quantity)

        return render_template("insight.html", names=names, values=values)
    return redirect(url_for("views.dashboard", user=current_user))


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

    tag = request.form["tag"]
    if not tag:
        flash("Missing keyword")
        return redirect(url_for("views.dashboard", user=current_user))

    search = "%{}%".format(tag)
    location_filter = User.query.filter(User.location.like(search)).one_or_none()

    if location_filter is None:
        businessname_filter = User.query.filter(User.businessname.like(search)).one_or_none()
        if businessname_filter is None:
            flash("Not found")
            return render_template('npo.html', businessname=current_user.businessname, food=[], users=[], tag=tag)

        businessname = User.query.filter(User.businessname.like(search)).all()
        for i in businessname:
            food = Food.query.filter_by(users_id=i.id).all()
            return render_template('npo.html',
                                    businessname=current_user.businessname,
                                    food=food,
                                    users=businessname,
                                    tag=tag)

    location = User.query.filter(User.location.like(search)).all()
    for i in location:
        food = Food.query.filter_by(users_id=i.id).all()
        return render_template('npo.html', businessname=current_user.businessname, food=food, users=location, tag=tag)


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
    # Show and Update items in restaurant page
    id = request.form.get("id")
    name = request.form.get("name")
    description = request.form.get("des")
    quantity = request.form.get("quantity")
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
