from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired(), Length(2, 45)])
    email = EmailField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired(), Length(8, 45)])
    confirm_password = PasswordField(
        "Confirm Password:", validators=[EqualTo("password", "passwords must match.")]
    )
