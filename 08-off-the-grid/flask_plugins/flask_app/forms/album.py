from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField
from wtforms.validators import DataRequired, Length


class AlbumForm(FlaskForm):
    title = StringField("Title:", validators=[DataRequired(), Length(2, 45)])
    artist = StringField("Artist:", validators=[DataRequired(), Length(2, 45)])
    user_id = HiddenField()
