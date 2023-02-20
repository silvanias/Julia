from datetime import datetime
from juliaapp.models import User

def test_landing_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200 

def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_login_content(client):
    # Returns landing content
    response = client.get('/login')
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password" id="password" placeholder="Password" required>' in response.data  

def test_signup_success(client):
    # Page loads
    response = client.get('/signup')
    assert response.status_code == 200

def test_signup_creates_user(client):
    # Creates a user
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    assert User.query.first() is not None

def test_signup_content(client):
    # Returns landing content
    response = client.get('/signup')
    assert b'<input type="text" name="username" id="username" placeholder="Username" required>' in response.data
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password1" id="password1" placeholder="Password" required>' in response.data
    assert b'<input type="password" name="password2" id="password2" placeholder="Confirm Password" required>' in response.data 


def test_generate_success(client):
    # Page loads
    response = client.get('/gen')
    assert response.status_code == 200