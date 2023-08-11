from pprint import pprint
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
