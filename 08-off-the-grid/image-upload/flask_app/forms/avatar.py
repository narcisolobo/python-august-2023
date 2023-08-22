from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField


class AvatarForm(FlaskForm):
    """Class to instantiate an Avatar Form."""

    avatar = FileField("Select Image:", validators=[FileRequired()])
