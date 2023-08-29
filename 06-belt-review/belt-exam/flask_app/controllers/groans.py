from flask_app import app
from flask_app.models.groan import Groan
from flask import redirect, request, session


@app.post("/groans/create")
def create_groan():
    """Processes the groan form."""

    Groan.create(request.form)

    return redirect("/jokes")
