from flask import Blueprint, redirect, render_template
from flask_app.forms.register import RegisterForm

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    return render_template("/main/index.html")
