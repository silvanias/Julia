from datetime import datetime
from juliaapp.models import User
from flask import request
# Test list need to be done:
    # Login takes you to your page 
    # Login puts your name in the footer
    # Logout logs you out 
    # Logged in users can see their own page
    # Invalid hex values break the page
    # delete_user route deletes a user
    # Test db constraints (delete user without deleting fractals)
    # Create a lock to prevent two users from grabbing colours at the same time

def test_login_content(client):
    # Returns landing content
    response = client.get('/login')
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password" id="password" placeholder="Password" required>' in response.data  

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


# Ask about this one!
def test_user_nonunique_email_fail(client):
    client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    assert b'<div class="alert error">' in response.data
    assert User.query.count() == 1

def test_signup_content(client):
    # Returns landing content
    response = client.get('/signup')
    assert b'<input type="text" name="username" id="username" placeholder="Username" required>' in response.data
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password1" id="password1" placeholder="Password" required>' in response.data
    assert b'<input type="password" name="password2" id="password2" placeholder="Confirm Password" required>' in response.data 

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

def test_generate_restricted(client, assertStatusCode2xx):
    response = client.get('/gen', follow_redirects=True)
    assert b'<title>Login</title>' in response.data
    assertStatusCode2xx(response.status_code) 