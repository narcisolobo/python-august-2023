from flask_app.models.album import Album
from flask_app.forms.album import AlbumForm
from flask_app.extensions import db
from flask_login import current_user
from flask import Blueprint, redirect, render_template, request

bp = Blueprint("albums", __name__, url_prefix="/albums")


@bp.route("/create", methods=["GET", "POST"])
def create_album():
    """Displays and processes the new album form."""

    form = AlbumForm(user_id=current_user.id)

    if form.validate_on_submit():
        # Get the valid user input
        title = request.form.get("title")
        artist = request.form.get("artist")
        user_id = request.form.get("user_id")

        new_album = Album(title=title, artist=artist, user_id=user_id)
        db.session.add(new_album)
        db.session.commit()
        return redirect("/albums")

    return render_template("/albums/new_album.html", form=form)


@bp.get("/")
def all_albums():
    """Displays all albums"""

    albums = Album.query.all()

    return render_template("/albums/all_albums.html", albums=albums)
