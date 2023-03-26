from dotenv import load_dotenv, find_dotenv
from os import environ

class Config():
    def __init__(self, database_url = None):
        load_dotenv(find_dotenv())
        self.SQLALCHEMY_DATABASE_URI: str = database_url or environ.get("DATABASE_URL")
        self.SECRET_KEY = environ.get("SECRET_KEY")
        self.FLASK_APP = environ.get("FLASK_APP")
        self.DEBUG = environ.get("DEBUG")