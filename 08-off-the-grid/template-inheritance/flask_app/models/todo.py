from datetime import date, datetime
from flask import flash
from flask_app.config.mysqlconnection import connect

DATABASE = "flask_todos_db"


class Todo:
    """Just one class - no relationships in this project."""

    def __init__(self, data):
        """Contructor function."""

        self.id = data["id"]
        self.task = data["task"]
        self.due_at = data["due_at"]
        self.is_complete = data["is_complete"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def create_form_is_valid(form_data):
        """Validates the todo form."""

        today = datetime.now()

        is_valid = True

        if len(form_data["task"].strip()) == 0:
            is_valid = False
            flash("Please enter your task.", "task")
        elif len(form_data["task"].strip()) < 2:
            is_valid = False
            flash("Task must be at least two characters.", "task")

        if form_data["due_at"] == "":
            is_valid = False
            flash("Please enter due date.", "due_at")
        else:
            due_at = datetime.strptime(form_data["due_at"], "%Y-%m-%d")
            if due_at < today:
                is_valid = False
                flash("Due date must be in the future.", "due_at")

        if "is_complete" not in form_data:
            is_valid = False
            flash("Please select yes or no.", "is_complete")

        return is_valid

    @staticmethod
    def update_form_is_valid(form_data):
        """Validates the todo form."""

        is_valid = True

        if len(form_data["task"].strip()) == 0:
            is_valid = False
            flash("Please enter your task.", "task")
        elif len(form_data["task"].strip()) < 2:
            is_valid = False
            flash("Task must be at least two characters.", "task")

        if "is_complete" not in form_data:
            is_valid = False
            flash("Please select yes or no.", "is_complete")

        return is_valid

    @classmethod
    def create(cls, form_data):
        query = """
        INSERT INTO todos (task, due_at)
        VALUES (%(task)s, %(due_at)s);
        """

        todo_id = connect(DATABASE).query_db(query, form_data)
        return todo_id

    @classmethod
    def get_all(cls):
        """Retrieves all todos from the database."""

        query = "SELECT * FROM todos;"

        results = connect(DATABASE).query_db(query)

        todos = []
        for result in results:
            todos.append(Todo(result))

        return todos

    @classmethod
    def get_one(cls, todo_id):
        """Retrieves one todo from the database by ID."""

        query = """
        SELECT * FROM todos
        WHERE id = %(todo_id)s;
        """

        data = {"todo_id": todo_id}

        results = connect(DATABASE).query_db(query, data)
        return Todo(results[0])

    @classmethod
    def update(cls, form_data):
        """Updates a todo in the database."""

        query = """
        UPDATE todos
        SET task = %(task)s, is_complete = %(is_complete)s
        WHERE id = %(todo_id)s;
        """

        connect(DATABASE).query_db(query, form_data)
        return

    @classmethod
    def toggle(cls, todo_id):
        """Toggles a todo in the database."""

        query = """
        UPDATE todos
        SET is_complete = NOT is_complete
        WHERE id = %(todo_id)s;
        """

        data = {"todo_id": todo_id}

        connect(DATABASE).query_db(query, data)
        return

    @classmethod
    def delete(cls, todo_id):
        """Deletes a todo in the database."""

        query = """
        DELETE FROM todos
        WHERE id = %(todo_id)s;
        """

        data = {"todo_id": todo_id}

        connect(DATABASE).query_db(query, data)
        return
