#https://codecookies.xyz/flask-2-tutorial/v1/unit-testing/
import pytest
from juliaapp.app import create_app
from os import environ
from flask_migrate import upgrade

@pytest.fixture
def client():
    environ["DATABASE_URL"] = 'sqlite://'
    app = create_app()

    with app.app_context():
        upgrade()
        yield app.test_client()