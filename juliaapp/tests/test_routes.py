from juliaapp.models import User
from juliaapp.tests.scripts_for_testing import login

def test_signup_creates_user(client):
    # Creates a user
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    assert User.query.count() == 1

def test_user_profile_page_redirect(client):
    # Create a user
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    }, follow_redirects=True)
    assert response.request.path == "/profile/test"
    assert b'<div class="logout">' in response.data
    assert b'user@test.com' in response.data
    assert b'<a href="/logout">Logout</a>' in response.data

def test_user_created_flash(client):
    # Create a user
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    }, follow_redirects=True)
    assert b'<div class="alert success">' in response.data
    assert b'User Created!' in response.data 

def test_logout_user_route(client):
    login(client)
    response = client.get('/logout', follow_redirects=True)
    client.get('/login', follow_redirects=True) 
    assert b'<title>Login</title>' in response.data
    assert b'<div class="logout">' not in response.data

def test_delete_user_route(client):
    client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'})
    #login(client)
    response = client.get('/delete_user', follow_redirects=True)
    assert b'<title>Landing</title>' in response.data

def test_user_nonunique_email_fail(client):
    user1 = User(username='test', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00)).save()
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    assert b'<div class="alert error">' in response.data
    assert User.query.count() == 1

def test_signup_flash_not_matched_passwords(client):
    # Pass bad data
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password11'
    }, follow_redirects=True) 
    assert b'<div class="alert error">' in response.data
    assert b'Passwords must match' in response.data


from datetime import datetime 
from unittest.mock import PropertyMock, patch

def test_gen_invalid_hexes(client):
    # Create user
    user1 = User(username='test1', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user1.save()

    # Mock current_user
    with patch('flask_login.utils._get_user', new_callable=PropertyMock) as get_user:
        get_user.return_value = user1

        # Pass bad data
        response = client.post('/gen', data={
            'hexval':'ZZZZZZ',
            'sets':'mandelbrot'
        })

    assert b'<div class="alert error">' in response.data
    assert b'Please enter a valid hex value' in response.data