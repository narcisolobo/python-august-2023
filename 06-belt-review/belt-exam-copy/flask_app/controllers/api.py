
from flask_app import app
from flask_app.models.user import User
from flask_app.models.joke import Joke
from flask import flash, redirect, render_template, request, session


@app.get("/jokes")
def api_all_jokes():
    """Displays the all_jokes template."""

    if "user_id" not in session or session["user_id"] == False:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.get_by_user_id(session["user_id"])
    jokes = Joke.get_all_with_users()
    print("SESSION USER_ID:", session["user_id"])

    return render_template("all_jokes.html", user=user, jokes=jokes)


@app.post("/api/jokes/create")
def api_create_joke():
    """Processes the new joke form."""

    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    if not Joke.form_is_valid(request.form):
        return redirect("/jokes/new")

    joke_id = Joke.create(request.form)
    joke = Joke.get_one(joke_id)
    return vars(joke)

@app.post("/jokes/<int:joke_id>/delete")
def api_delete_joke(joke_id):
    """Deletes a joke by id."""

    Joke.delete_joke(joke_id)

    return redirect("/jokes")
