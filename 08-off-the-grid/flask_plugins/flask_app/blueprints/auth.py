from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, login_user, logout_user

from flask_app.extensions import bcrypt, db, login_manager
from flask_app.forms.login import LoginForm
from flask_app.forms.register import RegisterForm
from flask_app.models.user import User

bp = Blueprint("auth", __name__)

login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    """User loader for Flask-Login."""

    return User.query.get(int(user_id))


@bp.route("/auth/register", methods=["GET", "POST"])
def register():
    """Displays the register page."""

    form = RegisterForm()

    if form.validate_on_submit():
        # Get valid user input
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the user's email exists
        potential_user = User.query.filter_by(email=email).first()
        if potential_user:
            flash("Email in use. Please log in.", "warning")
            return redirect("/auth/login")

        # Hash the password
        hashed = bcrypt.generate_password_hash(password)

        # Create user, add to db
        new_user = User(username=username, email=email, password=hashed)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.", "success")
        return redirect("/auth/login")

    return render_template("/auth/register.html", form=form)


@bp.route("/auth/login", methods=["GET", "POST"])
def login():
    """Displays the login page."""

    form = LoginForm()

    if form.validate_on_submit():
        # Get the valid user input
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user's email exists
        potential_user = User.query.filter_by(email=email).first()
        if not potential_user:
            flash("Invalid credentials.")
            return redirect("/auth/login")

        user = potential_user

        # Check password validity
        if not bcrypt.check_password_hash(user.password, password):
            flash("Invalid credentials.")
            return redirect("/auth/login")

        # Log the user in
        login_user(user)
        return redirect("/albums")

    return render_template("/auth/login.html", form=form)


@bp.get("/auth/logout")
def logout():
    """Logs out the current user."""

    logout_user()
    return redirect("/")
