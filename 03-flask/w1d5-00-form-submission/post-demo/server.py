from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """Displays the index.html template."""

    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    """Processes the form."""

    print(request.form)
    print(request.form["username"].center(50, "*"))

    # always return a redirect on a post request
    # a redirect takes a route as an argument
    return redirect("/success")


@app.route("/success")
def success():
    """Display the success.html template."""

    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
