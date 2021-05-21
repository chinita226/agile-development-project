import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Food, User, Order, OrderDetails

views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to home page."""
    if current_user.is_authenticated:
        return redirect(
            url_for(
                'views.dashboard',
                user=current_user,
                username=current_user.username
            )
        )

    return redirect(
        url_for('views.about', user=current_user)
    )


@views.route('/about')
def about():
    """Route to home page."""
    return render_template("about.html", user=current_user)


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

        return render_template(
            "insight.html",
            names=names,
            values=values,
            user=current_user)

    return redirect(
        url_for("views.dashboard",
                user=current_user,
                username=current_user.username))


@views.route('/food-waste')
def blog():
    return render_template(
        "blog.html",
        user=current_user
        )


@views.route('/<username>')
@login_required
def dashboard(username):
    # Show restaurant page
    if current_user.user_type == 'restaurant':

        food = Food.query.filter_by(users_id=current_user.id).all()
        return render_template(
            'restaurant.html',
            businessname=current_user.businessname,
            food=food,
            user=current_user)

    food = Food.query.order_by(Food.food_name)
    users = User.query.all()
    orders = Order.query.filter_by(user_id=current_user.id)
    details = OrderDetails.query.all()
    # Show NPO page
    return render_template(
        'npo.html',
        businessname=current_user.businessname,
        food=food,
        users=users,
        user=current_user,
        orders=orders,
        details=details
        )


@views.route('/search', methods=["POST"])
@login_required
def npo_search():

    tag = request.form["tag"]
    orders = Order.query.filter_by(user_id=current_user.id)
    # details = OrderDetails.query.all()
    if not tag:
        flash("Missing keyword")
        return redirect(url_for("views.dashboard", user=current_user, username=current_user.username))

    search = "%{}%".format(tag)
    location_filter = User.query.filter(User.location.like(search)).one_or_none()

    if location_filter is None:
        businessname_filter = User.query.filter(User.businessname.like(search)).one_or_none()
        if businessname_filter is None:
            flash("Not found")
            return render_template('npo.html', businessname=current_user.businessname, food=[], user=[], tag=tag, )

        businessname = User.query.filter(User.businessname.like(search)).all()
        for i in businessname:
            food = Food.query.filter_by(users_id=i.id).all()
            details = OrderDetails.query.filter(Food.users_id == i.id).all()
            return render_template(
                'npo.html',
                businessname=current_user.businessname,
                food=food, users=businessname,
                tag=tag, orders=orders,
                details=details,
                user=current_user)

    location = User.query.filter(User.location.like(search)).all()
    for i in location:
        food = Food.query.filter_by(users_id=i.id).all()
        details = OrderDetails.query.filter(Food.users_id == i.id).all()
        return render_template(
                'npo.html',
                businessname=current_user.businessname,
                food=food, users=location,
                tag=tag, orders=orders,
                details=details,
                user=current_user)


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
    return render_template(
        'restaurant.html',
        businessname=current_user.businessname,
        food=food,
        user=current_user
        )


# Changed the code
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

    return redirect(
        url_for("views.dashboard",
                user=current_user,
                username=current_user.username))


@views.route("/delete", methods=["POST"])
@login_required
def delete():
    # Show and delete items in restaurant page
    id = request.form.get("id")
    Food.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Item deleted!")
    Food.query.all()
    return redirect(
        url_for("views.dashboard",
                user=current_user,
                username=current_user.username))


@views.route("/order", methods=["POST"])
@login_required
def create_order():

    date = datetime.datetime.now()
    order = Order(user_id=current_user.id, date=date)
    db.session.add(order)
    db.session.commit()

    order_id = db.session.query(Order).filter_by(date=date).first().id

    order_data = request.json

    for item in order_data:
        order_details = OrderDetails(
            food_id=item['id'],
            order_id=order_id,
            quantity=item['quantity']
        )
        db.session.add(order_details)

        food = Food.query.filter_by(id=item['id']).first()
        food.quantity -= int(item['quantity'])
        db.session.commit()

    return 'a response'
