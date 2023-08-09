from pprint import pprint

from flask import Flask, redirect, render_template, request

# import the class from friend.py
from friend import Friend

app = Flask(__name__)


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    pprint(friends)
    return render_template("index.html", friends=friends)


@app.route("/friends/<int:friend_id>")
def friend_details(friend_id):
    """Displays the details of one friend."""

    friend = Friend.get_one(friend_id)
    return render_template("details.html", friend=friend)


@app.get("/friends/new")
def new_friend():
    """Displays the new friend form template."""

    return render_template("new.html")


@app.post("/friends/create")
def create_friend():
    """Processes the submitted new friend form and creates a friend."""

    friend_id = Friend.create(request.form)
    # a redirect takes in a route
    return redirect(f"/friends/{friend_id}")


@app.get("/friends/<int:friend_id>/edit")
def edit_friend(friend_id):
    """Displays the the edit friend form template."""

    friend = Friend.get_one(friend_id)
    return render_template("edit.html", friend=friend)


@app.post("/friends/<int:friend_id>/update")
def update_friend(friend_id):
    """Processes the submitted edit form and updates a friend."""

    Friend.update(request.form)
    return redirect(f"/friends/{friend_id}")


@app.post("/friends/<int:friend_id>/delete")
def delete_friend(friend_id):
    """Delete a friend. :("""

    Friend.delete(friend_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
