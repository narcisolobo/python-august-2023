# server
# import the app from flask_app
from flask_app import app

# DON'T FORGET TO IMPORT YOUR CONTROLLERS
import flask_app.controllers.albums
import flask_app.controllers.songs

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
