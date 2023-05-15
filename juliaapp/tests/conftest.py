#https://codecookies.xyz/flask-2-tutorial/v1/unit-testing/
import pytest
from juliaapp.app import create_app
from juliaapp.extensions.database import db
from juliaapp.config import Config
from os import environ
from flask_migrate import upgrade
from dotenv.main import load_dotenv

@pytest.fixture
def config():
    # Return config to use in tests 
    # Use in-memory sqlite database making changes not permanent across tests
    return Config(
        database_url = 'sqlite://',
        testing = True
    ) 

@pytest.fixture
def app(config):
    # Create app using test config
    return create_app(config)

@pytest.fixture
def client(app):
    with app.app_context():
        upgrade()
        yield app.test_client()
        db.drop_all()

@pytest.fixture
def assertStatusCode2xx():
    def assertStatusCode2xx(status_code: int):
        assert status_code >= 200
        assert status_code < 300
        
    return assertStatusCode2xx


@pytest.fixture
def e2e_host(app):
    """
    Load the base url to make requests to in End-to-End tests from the .env file or environment variables.
    """
    load_dotenv()
    port = environ.get("E2E_APP_PORT", "")
    with app.app_context():
        upgrade()
        yield app.test_client()