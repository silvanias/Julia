#https://codecookies.xyz/flask-2-tutorial/v1/unit-testing/
import pytest
from juliaapp.app import create_app
from os import environ
from flask_migrate import upgrade
from dotenv.main import load_dotenv

@pytest.fixture
def client():
    environ["DATABASE_URL"] = 'sqlite://'
    app = create_app()

    with app.app_context():
        upgrade()
        yield app.test_client()

@pytest.fixture
def assertStatusCode2xx():
    def assertStatusCode2xx(status_code: int):
        assert status_code >= 200
        assert status_code < 300
        
    return assertStatusCode2xx 