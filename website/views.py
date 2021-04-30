from flask import Blueprint, render_template, request, flash
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    """Route to home page."""
    return render_template("about.html")

@views.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

