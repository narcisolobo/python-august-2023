import datetime
from flask_app import app
from flask_app.models.user import User
from flask_app.models.joke import Joke
from flask_app.models.groan import Groan
from flask import flash, redirect, render_template, request, session


@app.template_filter("format_date")
def format_date(date):
    return date.strftime("%B %-d, %Y")


@app.get("/jokes")
def all_jokes():
    """Displays the all_jokes template."""

    if "user_id" not in session or session["user_id"] == False:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_by_user_id(session["user_id"])
    jokes = Joke.get_all_with_users()
    print("SESSION USER_ID:", session["user_id"])

    return render_template("all_jokes.html", user=user, jokes=jokes)


@app.get("/jokes/new")
def new_joke():
    """Displays the new joke template."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_by_user_id(session["user_id"])

    return render_template("new_joke.html", user=user)


@app.post("/jokes/create")
def create_joke():
    """Processes the new joke form."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    if not Joke.form_is_valid(request.form):
        return redirect("/jokes/new")

    Joke.create(request.form)
    return redirect("/jokes")


@app.get("/jokes/<int:joke_id>")
def joke_details(joke_id):
    """Displays the joke_details template."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_by_user_id(session["user_id"])
    joke = Joke.get_one_with_user(joke_id)
    count = Groan.get_groan_count(joke_id)

    return render_template("joke_details.html", user=user, joke=joke, count=count)


@app.get("/jokes/<int:joke_id>/edit")
def edit_joke(joke_id):
    """Displays the edit_joke template."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_by_user_id(session["user_id"])
    joke = Joke.get_one_with_user(joke_id)

    return render_template("edit_joke.html", user=user, joke=joke)


@app.post("/jokes/<int:joke_id>/update")
def update_joke(joke_id):
    """Processes the edit joke form."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    Joke.update_joke(request.form)
    return redirect(f"/jokes/{joke_id}")


@app.post("/jokes/<int:joke_id>/delete")
def delete_joke(joke_id):
    """Deletes a joke by id."""

    Joke.delete_joke(joke_id)

    return redirect("/jokes")
