from random import randint

from flask import redirect, render_template, request

from flask_app import app
from flask_app.models.madlib import Madlib


@app.get("/")
def index():
    """Redirects the user to the form."""

    return redirect("/madlibs/new")


@app.get("/madlibs/new")
def new_madlib():
    """Displays the new Madlib form."""

    return render_template("/new_madlib.html")


@app.post("/madlibs/create")
def create_madlib():
    """Processes the new Madlib form."""

    madlib_id = Madlib.create(request.form)

    return redirect(f"/madlibs/{madlib_id}")


@app.get("/madlibs/<int:madlib_id>")
def madlib_details(madlib_id):
    """Displays the Madlib form results template."""

    madlib = Madlib.get_one(madlib_id)
    print(madlib.adjective)
    print(madlib.first_name)

    return render_template("madlib_details.html", madlib=madlib)


@app.get("/madlibs/random")
def random_madlib():
    """Picks a random Madlib ID and redirects to details."""

    all_madlibs = Madlib.get_all()
    random_id = randint(1, len(all_madlibs))

    return redirect(f"/madlibs/{random_id}")
