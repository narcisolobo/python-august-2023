import os

from flask import Blueprint, current_app, redirect, render_template, request
from flask_login import current_user, login_required

from flask_app.extensions import db
from flask_app.forms.avatar import AvatarForm
from flask_app.models.user import User
from flask_app.utilities import safe_unique_name

bp = Blueprint("profiles", __name__, url_prefix="/profiles")


@bp.route("/<int:user_id>", methods=["GET", "POST"])
@login_required
def profile(user_id):
    """Displays the current user's profile."""

    form = AvatarForm()

    if form.validate_on_submit():
        avatar = form.avatar.data
        safe_name = safe_unique_name(avatar.filename)
        avatar.save(os.path.join(current_app.config["UPLOAD_FOLDER"], safe_name))

        user = User.query.get(user_id)
        user.profile_pic = safe_name
        db.session.add(user)
        db.session.commit()

        return redirect(f"/profiles/{user_id}")

    return render_template("/profiles/profile.html", form=form)
