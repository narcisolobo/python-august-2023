from pprint import pprint
from flask_app.config.mysql_connection import connect_to_mysql

DATABASE = "vinyl_one_to_many"


class Song:
    def __init__(self, data):
        self.id = data["id"]
        self.number = data["number"]
        self.title = data["title"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.album_id = data["album_id"]

    # Create
    @classmethod
    def create(cls, form_data):
        """Create an song in the songs table."""

        query = """
        INSERT INTO songs (title, number, album_id)
        VALUES (%(title)s, %(number)s, %(album_id)s);
        """

        song_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return song_id

    # Read All
    @classmethod
    def get_all(cls):
        """Retrieve all songs in the songs table."""

        query = "SELECT * FROM songs;"

        results = connect_to_mysql(DATABASE).query_db(query)
        pprint(results)

        songs = []

        for dictionary in results:
            songs.append(Song(dictionary))

        return songs

    # Read One
    @classmethod
    def get_one(cls, song_id):
        """Retrieve one song from the songs table."""

        query = """
        SELECT * FROM songs
        WHERE id = %(song_id)s;
        """

        data = {"song_id": song_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)
        song = Song(results[0])
        return song

    # Update
    @classmethod
    def update(cls, form_data):
        """Update one song in the songs table."""

        query = """
        UPDATE songs
        SET title=%(title)s, number=%(number)s, album_id=%(album_id)s
        WHERE id = %(song_id)s;
        """

        connect_to_mysql(DATABASE).query_db(query, form_data)
        return

    # Delete
    @classmethod
    def delete(cls, song_id):
        """Delete one song in the songs table."""

        query = "DELETE FROM songs WHERE id = %(song_id)s;"

        data = {"song_id": song_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return
