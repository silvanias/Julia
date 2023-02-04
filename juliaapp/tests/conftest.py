#https://codecookies.xyz/flask-2-tutorial/v1/unit-testing/
import pytest
from juliaapp.app import create_app

@pytest.fixture
def client():
    app = create_app()

    with app.app_context():
        yield app.test_client()