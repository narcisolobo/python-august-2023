from flask_app import app
from datetime import datetime
from flask_app.models.todo import Todo
from flask import redirect, render_template, request


@app.template_filter("date_input")
def date_input_format(date):
    return date.strftime("%Y-%m-%d")


@app.get("/")
def index():
    """Redirects the user to /todos."""

    return redirect("/todos")


@app.get("/todos")
def all_todos():
    """Renders the all_todos.html template."""

    todos = Todo.get_all()
    return render_template("all_todos.html", todos=todos)


@app.get("/todos/new")
def new_todo():
    """Renders the new_todo.html template."""

    return render_template("new_todo.html")


@app.post("/todos/create")
def create_todo():
    """Processes the new_todo form."""

    print(request.form)

    if not Todo.create_form_is_valid(request.form):
        return redirect("/todos/new")

    Todo.create(request.form)
    return redirect("/todos")


@app.get("/todos/<int:todo_id>/edit")
def edit_todo(todo_id):
    """Renders the edit_todo.html template."""

    todo = Todo.get_one(todo_id)

    return render_template("edit_todo.html", todo=todo)


@app.post("/todos/<int:todo_id>/update")
def update_todo(todo_id):
    """Processes the edit todo form."""

    if not Todo.update_form_is_valid(request.form):
        return redirect(f"/todos/{todo_id}/edit")

    Todo.update(request.form)

    return redirect("/todos")


@app.post("/todos/<int:todo_id>/toggle")
def toggle_todo(todo_id):
    """Processes the edit todo form."""

    Todo.toggle(todo_id)

    return redirect("/todos")


@app.get("/todos/<int:todo_id>")
def todo_details(todo_id):
    """Renders the todo_details.html template."""

    todo = Todo.get_one(todo_id)

    return render_template("todo_details.html", todo=todo)


@app.post("/todos/<int:todo_id>/delete")
def delete_todo(todo_id):
    """Processes the delete form."""

    Todo.delete(todo_id)

    return redirect("/todos")
