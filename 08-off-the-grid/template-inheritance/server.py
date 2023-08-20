from flask_app import app

import flask_app.controllers.todos

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5002)
