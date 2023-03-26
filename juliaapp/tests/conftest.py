#https://codecookies.xyz/flask-2-tutorial/v1/unit-testing/
import pytest
from juliaapp.app import create_app
from juliaapp.extensions.database import db
from os import environ
from flask_migrate import upgrade
from dotenv.main import load_dotenv

@pytest.fixture
def config():
    """
    Define the default config to use in tests by default.

    Instead of a persistent postgresql, tests use an in-memory sqlite database by default. This way, changes aren't persisted across test runs.
    """
    environ["DATABASE_URL"] = 'sqlite://' 

@pytest.fixture
def app(config):
    """
    Create an app using the test config.
    """
    return create_app(config)

@pytest.fixture
def client(app):
    #environ["DATABASE_URL"] = 'sqlite://'
    #app = create_app()

    with app.app_context():
        upgrade()
        yield app.test_client()
        db.drop_all()

@pytest.fixture
def e2e_host():
    """
    Load the base url to make requests to in End-to-End tests from the .env file or environment variables.
    """
    load_dotenv()
    port = environ.get("E2E_APP_PORT", "")
    return "http://localhost:" + port

@pytest.fixture
def assertStatusCode2xx():
    def assertStatusCode2xx(status_code: int):
        assert status_code >= 200
        assert status_code < 300
        
    return assertStatusCode2xx 