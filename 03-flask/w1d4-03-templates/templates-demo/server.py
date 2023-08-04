from flask import Flask, render_template

app = Flask(__name__)

# A URL consists of two parts:
# The domain, and the path
# http://localhost:5000 - domain
# anything after the domain is the path (route)


@app.route("/")
def index():
    """This is the root route."""

    name = "Narciso"

    return render_template("index.html", banana=name)


@app.route("/<person>")
def greet_person(person):
    """
    This is a dynamic route that displays the name
    passed into the URL.
    """

    return render_template("index.html", banana=person)


@app.route("/<time_of_day>/<person>")
def greet_person_with_time(time_of_day, person):
    """Greet a person with the time of day."""

    context = {"time_of_day": time_of_day, "person": person}

    # return render_template("greet_time.html", time_of_day=time_of_day, person=person)
    return render_template("greet_time.html", **context)


@app.route("/muppets")
def list_muppets():
    """This displays a template that lists some Muppets."""

    muppets = [
        {"name": "Kermit the Frog", "location": "The swamp. I'm a frog."},
        {"name": "Miss Piggy", "location": "The green room. Where's my champagne?"},
        {"name": "Fozzie Bear", "location": "The Comedy Store - tonight at 8!"},
        {"name": "Gonzo the Great", "location": "Waiting to be shot out of a cannon."},
    ]

    return render_template("muppets.html", muppets=muppets)


@app.route("/age-checker/<int:age>")
def age_checker(age):
    """Display a template that checks if the user is over 21."""

    return render_template("age-checker.html", age=age)


@app.errorhandler(404)
def page_not_found(error):
    """Page not found custom error template."""

    return render_template("error.html", error=error)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
