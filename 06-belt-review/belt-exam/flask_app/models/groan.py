from flask import flash
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "belt_exam_db"


class Groan:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.joke_id = data["joke_id"]

    @classmethod
    def create(cls, form_data):
        """Inserts a new groan into the database."""

        query = """
        INSERT INTO groans (user_id, joke_id)
        VALUES (%(user_id)s, %(joke_id)s);
        """

        groan_id = connectToMySQL(DATABASE).query_db(query, form_data)
        print("GROAN ID:", groan_id)
        return groan_id

    @classmethod
    def get_all_by_joke_id(cls, joke_id):
        """
        Retrieves all groan rows from the database
        including the users who created them.
        """

        query = """
        SELECT * FROM groans
        WHERE joke_id = %(joke_id)s;
        """

        data = {"joke_id": joke_id}

        results = connectToMySQL(DATABASE).query_db(query, data)

        groans = []

        for result in results:
            groan = Groan(result)
            groans.append(groan)

        return groans

    @classmethod
    def get_one_with_user(cls, groan_id):
        """
        Retrieves one groan row from the database
        including the user who created it.
        """

        query = """
        SELECT * FROM groans
        JOIN users
        ON groans.user_id = users.id
        WHERE groans.id = %(groan_id)s;
        """

        data = {"groan_id": groan_id}

        results = connectToMySQL(DATABASE).query_db(query, data)
        groan = Groan(results[0])
        creator = user.User.get_by_user_id(results[0]["user_id"])
        groan.user = creator

        return groan

    @classmethod
    def update_groan(cls, form_data):
        """Updates one groan row in the database."""

        query = """
        UPDATE groans
        SET setup = %(setup)s, punchline = %(punchline)s
        WHERE id = %(groan_id)s;
        """

        connectToMySQL(DATABASE).query_db(query, form_data)
        return

    @classmethod
    def delete_groan(cls, groan_id):
        """Deletes one groan row from the database."""

        query = """
        DELETE FROM groans
        WHERE id = %(groan_id)s;
        """

        data = {"groan_id": groan_id}

        connectToMySQL(DATABASE).query_db(query, data)
        return

    @classmethod
    def get_groan_count(cls, joke_id):
        """Return the groan count of a joke."""

        query = """
        SELECT COUNT(joke_id) as 'count'
        FROM groans
        WHERE joke_id = %(joke_id)s;
        """

        data = {"joke_id": joke_id}

        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]["count"]
