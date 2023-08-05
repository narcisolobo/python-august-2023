import math
import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "a89d0ce61d1813282d669e511b016a15490f819c8a60d48ca77189195af87bb1"


@app.route("/")
def index():
    """Displays the index.html template."""

    session["method_name"] = "index"
    session["random_number"] = math.floor(random.random() * 10)

    if "username" not in session:
        session["username"] = "guest"

    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    """Processes the form."""

    print(request.form)
    print(request.form["username"])

    session["username"] = request.form["username"]

    # always return a redirect on a post request
    # a redirect takes a route as an argument
    return redirect("/success")


@app.route("/success")
def success():
    """Display the success.html template."""

    return render_template("success.html")


@app.route("/clear-session")
def clear_session():
    """Clears the session data."""

    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
