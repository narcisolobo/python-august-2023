from os import environ
from flask import Flask
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY")
