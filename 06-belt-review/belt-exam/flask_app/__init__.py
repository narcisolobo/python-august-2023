from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "f33be79b7bec90e979c5fcc8bb4a2ba06b43e1c3dcfecee4ba560f1e4d37cca4"

bcrypt = Bcrypt(app)
