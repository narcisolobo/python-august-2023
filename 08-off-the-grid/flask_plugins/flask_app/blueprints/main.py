from flask import Blueprint, redirect, render_template
from flask_app.forms.register import RegisterForm

bp = Blueprint("main", __name__)


@bp.get("/")
def redirect_user():
    return render_template("index.html")


@bp.get("/welcome")
def welcome():
    return render_template("welcome.html")
