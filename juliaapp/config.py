from dotenv import load_dotenv, find_dotenv
from os import environ

print(find_dotenv())
load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")