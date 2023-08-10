from pprint import pprint
from flask_app import app
from flask_app.models.album import Album
from flask_app.models.song import Song
from flask import redirect, render_template, request


@app.route("/songs")
def all_songs():
    """Displays all the songs."""

    songs = Song.get_all()

    return render_template("all_songs.html", songs=songs)


@app.route("/albums/<int:album_id>/songs/new")
def new_song(album_id):
    """Displays the new song form."""

    album = Album.get_one(album_id)

    return render_template("new_song.html", album=album)


@app.route("/songs/create", methods=["post"])
def create_song():
    """Process the new song form."""

    pprint(request.form)

    song_id = Song.create(request.form)

    print("**************", song_id, "******************")
    return redirect(f"/albums/{request.form['album_id']}")


@app.route("/songs/<int:song_id>")
def song_details(song_id):
    """Displays the details of one song."""

    song = Song.get_one(song_id)
    return render_template("song_details.html", song=song)


@app.route("/songs/<int:song_id>/edit")
def edit_song(song_id):
    """Displays the form to edit an song."""

    song = Song.get_one(song_id)

    return render_template("edit_song.html", song=song)


@app.route("/songs/<int:song_id>/update", methods=["POST"])
def update_song(song_id):
    """Processes the edit song form."""

    Song.update(request.form)

    return redirect(f"/songs/{song_id}")


@app.route("/songs/<int:song_id>/delete", methods=["POST"])
def delete_song(song_id):
    """Deletes an song. Processes the delete song form."""

    Song.delete(song_id)

    return redirect("/songs")
