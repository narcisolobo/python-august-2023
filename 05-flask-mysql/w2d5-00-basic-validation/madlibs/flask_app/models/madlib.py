from pprint import pprint
from flask import flash
from flask_app.config.mysql_connection import connect_to_mysql

DATABASE = "madlibs_db"


class Madlib:
    def __init__(self, data):
        self.id = data["id"]
        self.number = data["number"]
        self.noun = data["noun"]
        self.verb = data["verb"]
        self.adjective = data["adjective"]
        self.first_name = data["first_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def form_is_valid(form_data):
        is_valid = True
        # check if number has been entered
        if len(form_data["number"].strip()) == 0:
            is_valid = False
            flash("Please enter a number.")
        # check if number is positive
        elif int(form_data["number"]) < 0:
            is_valid = False
            flash("Number must be greater than zero.")

        # check if noun has been entered
        if len(form_data["noun"].strip()) == 0:
            is_valid = False
            flash("Please enter a noun.")
        # check if noun length is greater than two
        elif len(form_data["noun"].strip()) < 2:
            is_valid = False
            flash("Noun must be at least two characters.")

        # check if verb has been entered
        if len(form_data["verb"].strip()) == 0:
            is_valid = False
            flash("Please enter a verb.")
        # check if verb length is greater than two
        elif len(form_data["verb"].strip()) < 2:
            is_valid = False
            flash("Verb must be at least two characters.")

        # check if adjective has been entered
        if len(form_data["adjective"].strip()) == 0:
            is_valid = False
            flash("Please enter an adjective.")
        # check if adjective length is greater than two
        elif len(form_data["adjective"].strip()) < 2:
            is_valid = False
            flash("Adjective must be at least two characters.")

        # check if first name has been entered
        if len(form_data["first_name"].strip()) == 0:
            is_valid = False
            flash("Please enter an first name.")
        elif form_data["first_name"][0].islower():
            is_valid = False
            flash("Please enter a capitalized name.")

        return is_valid

    # Create
    @classmethod
    def create(cls, form_data):
        """Create a new madlib in the madlibs table."""

        query = """
        INSERT INTO madlibs (number, noun, verb, adjective, first_name)
        VALUES (%(number)s, %(noun)s, %(verb)s, %(adjective)s, %(first_name)s);
        """

        madlib_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return madlib_id

    # Read All
    @classmethod
    def get_all(cls):
        """Retrieve all madlibs in the madlibs table."""

        query = "SELECT * FROM madlibs;"

        results = connect_to_mysql(DATABASE).query_db(query)
        pprint(results)

        madlibs = []

        for dictionary in results:
            madlibs.append(Madlib(dictionary))

        return madlibs

    # Read One
    @classmethod
    def get_one(cls, madlib_id):
        """Retrieve one madlib from the madlibs table."""

        query = """
        SELECT * FROM madlibs
        WHERE id = %(madlib_id)s;
        """

        data = {"madlib_id": madlib_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)
        madlib = Madlib(results[0])
        return madlib

    # Update
    @classmethod
    def update(cls, form_data):
        """Update one madlib in the madlibs table."""

        query = """
        UPDATE madlibs
        SET number=%(number)s, noun=%(noun)s, verb=%(verb)s, adjective=%(adjective)s, first_name=%(first_name)s
        WHERE id = %(madlib_id)s;
        """

        connect_to_mysql(DATABASE).query_db(query, form_data)
        return

    # Delete
    @classmethod
    def delete(cls, madlib_id):
        """Delete one madlib in the madlibs table."""

        query = """
        DELETE FROM madlibs 
        WHERE id = %(madlib_id)s;
        """

        data = {"madlib_id": madlib_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return
