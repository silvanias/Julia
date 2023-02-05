from dotenv import load_dotenv, find_dotenv
from os import environ

load_dotenv(find_dotenv())
SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
SECRET_KEY = environ.get("SECRET_KEY")
FLASK_APP = environ.get("FLASK_APP")
DEBUG = environ.get("DEBUG")
