import requests
from pprint import pprint
from flask_app import app
from flask import redirect, render_template, request, session


@app.get("/")
def characters():
    """Displays the characters.html template."""

    if "url" not in session:
        session["url"] = "https://rickandmortyapi.com/api/character"

    response = requests.get(session["url"])

    json = response.json()

    characters = []

    for result in json["results"]:
        character = {
            "gender": result["gender"],
            "image": result["image"],
            "name": result["name"],
            "species": result["species"],
        }
        characters.append(character)

    info = {
        "prev": json["info"]["prev"],
        "next": json["info"]["next"],
    }

    print(info)

    return render_template("characters.html", characters=characters, info=info)


@app.post("/set-url")
def set_url():
    """Sets the current URL."""

    session["url"] = request.form["url"]
    return redirect("/")
