from flask_app import app

# DON'T FORGET TO IMPORT CONTROLLERS
import flask_app.controllers.users
import flask_app.controllers.jokes
import flask_app.controllers.groans
import flask_app.controllers.api

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
