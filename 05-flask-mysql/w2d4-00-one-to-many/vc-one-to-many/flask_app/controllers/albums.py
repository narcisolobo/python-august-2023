from pprint import pprint
from flask_app import app
from flask_app.models.album import Album
from flask import redirect, render_template, request


@app.route("/")
def index():
    """Renders the index.html template."""

    return render_template("index.html")


@app.route("/albums")
def all_albums():
    """Displays all the albums."""

    albums = Album.get_all()

    return render_template("all_albums.html", albums=albums)


@app.route("/albums/new")
def new_album():
    """Displays the new album form."""

    return render_template("new_album.html")


@app.route("/albums/create", methods=["post"])
def create_album():
    """Process the new album form."""

    pprint(request.form)

    album_id = Album.create(request.form)

    print("**************", album_id, "******************")
    return redirect("/albums")


@app.route("/albums/<int:album_id>")
def album_details(album_id):
    """Displays the details of one album."""

    album = Album.get_one_with_songs(album_id)
    return render_template("album_details.html", album=album)


@app.route("/albums/<int:album_id>/edit")
def edit_album(album_id):
    """Displays the form to edit an album."""

    album = Album.get_one(album_id)

    return render_template("edit_album.html", album=album)


@app.route("/albums/<int:album_id>/update", methods=["POST"])
def update_album(album_id):
    """Processes the edit album form."""

    Album.update(request.form)

    return redirect(f"/albums/{album_id}")


@app.route("/albums/<int:album_id>/delete", methods=["POST"])
def delete_album(album_id):
    """Deletes an album. Processes the delete album form."""

    Album.delete(album_id)

    return redirect("/albums")
