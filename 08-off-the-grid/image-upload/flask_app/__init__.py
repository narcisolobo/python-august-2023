from os import environ
from os.path import join, dirname, realpath

from dotenv import load_dotenv
from flask import Flask

from .blueprints.auth import bp as auth
from .blueprints.main import bp as main
from .blueprints.profiles import bp as profiles
from .extensions import bcrypt, db, login_manager

load_dotenv()

SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
BASE_DIR = join(dirname(realpath(__file__)))
UPLOAD_PATH = ["static", "images", "profile_pictures"]
UPLOAD_FOLDER = join(BASE_DIR, *UPLOAD_PATH)


def create_app():
    """Flask app factory."""

    # App configurations
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    # Initialize extensions
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(profiles)

    # Create db tables
    with app.app_context():
        from flask_app.models.user import User

        db.create_all()

    return app
