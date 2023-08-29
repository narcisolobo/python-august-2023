from flask import flash
from flask_app.models import user
from flask_app.models import groan
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "belt_exam_db"


class Joke:
    def __init__(self, data):
        self.id = data["id"]
        self.setup = data["setup"]
        self.punchline = data["punchline"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def form_is_valid(form_data):
        """Validates the joke form."""

        is_valid = True

        if len(form_data["setup"].strip()) == 0:
            is_valid = False
            flash("Please enter setup.", "setup")
        elif len(form_data["setup"].strip()) < 3:
            is_valid = False
            flash("Setup must be at least 2 characters.")

        if len(form_data["setup"].strip()) == 0:
            is_valid = False
            flash("Please enter punchline.", "punchline")
        elif len(form_data["punchline"].strip()) < 3:
            is_valid = False
            flash("Punchline must be at least 2 characters.")

        return is_valid

    def is_groaned_at_by(self, user_id):
        """Returns true or false if user groaned at joke."""

        has_groaned = False
        groans = groan.Groan.get_all_by_joke_id(self.id)
        for g in groans:
            if g.user_id == user_id:
                has_groaned = True
        return has_groaned

    @classmethod
    def create(cls, form_data):
        """Inserts a new joke into the database."""

        query = """
        INSERT INTO jokes (setup, punchline, user_id)
        VALUES (%(setup)s, %(punchline)s, %(user_id)s);
        """

        joke_id = connectToMySQL(DATABASE).query_db(query, form_data)
        return joke_id

    @classmethod
    def get_all_with_users(cls):
        """
        Retrieves all joke rows from the database
        including the users who created them.
        """

        query = """
        SELECT * FROM jokes
        JOIN users
        ON jokes.user_id = users.id;
        """

        results = connectToMySQL(DATABASE).query_db(query)

        jokes = []

        for result in results:
            joke = Joke(result)
            creator = user.User.get_by_user_id(result["user_id"])
            joke.user = creator
            jokes.append(joke)

        return jokes

    @classmethod
    def get_one_with_user(cls, joke_id):
        """
        Retrieves one joke row from the database
        including the user who created it.
        """

        query = """
        SELECT * FROM jokes
        JOIN users
        ON jokes.user_id = users.id
        WHERE jokes.id = %(joke_id)s;
        """

        data = {"joke_id": joke_id}

        results = connectToMySQL(DATABASE).query_db(query, data)
        joke = Joke(results[0])
        creator = user.User.get_by_user_id(results[0]["user_id"])
        joke.user = creator

        return joke

    @classmethod
    def update_joke(cls, form_data):
        """Updates one joke row in the database."""

        query = """
        UPDATE jokes
        SET setup = %(setup)s, punchline = %(punchline)s
        WHERE id = %(joke_id)s;
        """

        connectToMySQL(DATABASE).query_db(query, form_data)
        return

    @classmethod
    def delete_joke(cls, joke_id):
        """Deletes one joke row from the database."""

        query = """
        DELETE FROM jokes
        WHERE id = %(joke_id)s;
        """

        data = {"joke_id": joke_id}

        connectToMySQL(DATABASE).query_db(query, data)
        return
