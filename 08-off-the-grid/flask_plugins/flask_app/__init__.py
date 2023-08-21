from os import environ
from flask import Flask
from flask_app.blueprints.main import bp as main
from flask_app.blueprints.auth import bp as auth
from flask_app.blueprints.albums import bp as albums
from flask_app.extensions import bcrypt, db, login_manager
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")


def create_app():
    """Flask app factory."""

    # App configuration
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(albums)

    # Initialize Extensions
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from flask_app.models.user import User
        from flask_app.models.album import Album

        db.create_all()

    return app
