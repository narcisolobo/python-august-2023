# import the function that will return an instance of a connection
from pprint import pprint
from mysql_connection import connect_to_mysql

DATABASE = "friends_db"


# model the class after the friend table from our database
class Friend:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.occupation = data["occupation"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def __repr__(self) -> str:
        return f"<Friend: {self.first_name} {self.last_name}>"

    @classmethod
    def create(cls, form_data):
        """Creates a new friend row in the friends table."""

        query = """
        INSERT INTO friends (first_name, last_name, occupation)
        VALUES (%(first_name)s, %(last_name)s, %(occupation)s);
        """

        friend_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return friend_id

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connect_to_mysql function with the schema you are targeting.
        results = connect_to_mysql(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dictionary in results:
            friends.append(Friend(dictionary))
        return friends

    @classmethod
    def get_one(cls, friend_id):
        query = """
        SELECT * FROM friends
        WHERE id = %(friend_id)s;
        """

        data = {"friend_id": friend_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)
        friend = Friend(results[0])
        return friend

    @classmethod
    def update(cls, form_data):
        """Update a row in the friends table."""

        query = """
        UPDATE friends
        SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s
        WHERE id = %(friend_id)s;
        """

        connect_to_mysql(DATABASE).query_db(query, form_data)
        return

    @classmethod
    def delete(cls, friend_id):
        """Deletes a row in the friends table."""

        query = "DELETE FROM friends WHERE id = %(friend_id)s;"

        data = {"friend_id": friend_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return
