from pprint import pprint
from flask_app.models.song import Song
from flask_app.config.mysql_connection import connect_to_mysql

DATABASE = "vinyl_one_to_many"


class Album:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.artist = data["artist"]
        self.genre = data["genre"]
        self.is_owned = data["is_owned"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.songs = []

    # Create
    @classmethod
    def create(cls, form_data):
        """Create an album in the albums table."""

        query = """
        INSERT INTO albums (title, artist, genre)
        VALUES (%(title)s, %(artist)s, %(genre)s);
        """

        album_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return album_id

    # Read All
    @classmethod
    def get_all(cls):
        """Retrieve all albums in the albums table."""

        query = "SELECT * FROM albums;"

        results = connect_to_mysql(DATABASE).query_db(query)
        pprint(results)

        albums = []

        for dictionary in results:
            albums.append(Album(dictionary))

        return albums

    # Read One
    @classmethod
    def get_one(cls, album_id):
        """Retrieve one album from the albums table."""

        query = """
        SELECT * FROM albums
        WHERE id = %(album_id)s;
        """

        data = {"album_id": album_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)
        album = Album(results[0])
        return album

    # Read One
    @classmethod
    def get_one_with_songs(cls, album_id):
        """Retrieve one album and all of its songs from the database."""

        query = """
        SELECT * FROM albums
        LEFT JOIN songs
        ON songs.album_id = albums.id
        WHERE albums.id = %(album_id)s;
        """

        data = {"album_id": album_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)

        pprint(results)

        album = Album(results[0])

        for result in results:
            if result["songs.id"]:
                song = Song.get_one(result["songs.id"])
                album.songs.append(song)

        return album

    # Update
    @classmethod
    def update(cls, form_data):
        """Update one album in the albums table."""

        query = """
        UPDATE albums
        SET title=%(title)s, artist=%(artist)s, genre=%(genre)s, is_owned=%(is_owned)s
        WHERE id = %(album_id)s;
        """

        connect_to_mysql(DATABASE).query_db(query, form_data)
        return

    # Delete
    @classmethod
    def delete(cls, album_id):
        """Delete one album in the albums table."""

        query = """
        DELETE FROM albums 
        WHERE id = %(album_id)s;
        """

        data = {"album_id": album_id}

        connect_to_mysql(DATABASE).query_db(query, data)
        return
