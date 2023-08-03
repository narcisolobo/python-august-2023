from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """
    This is the index route handler (view function, controller)
    This is also a static route.
    """

    return "<h1>Hello world!</h1>"


@app.route("/<name>")
def greet_name(name):
    """
    Dynamic route that maps to this view function.
    Remember to include the angle brackets in the decorator
    and pass it into the function's parameters.
    """

    return f"<h1>This is the first route: {name}</h1>"


@app.route("/multiply/<int:operand>")
def multiply(operand):
    """
    Take the operand passed into the route,
    multiply it by 2 and return it to the browser.
    """

    product = operand * 2
    return f"{product}"


# @app.errorhandler(404)
# def not_found(e):
#     return "hello buddy."


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
