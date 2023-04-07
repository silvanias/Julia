from flask_login import FlaskLoginClient
from juliaapp.models import User

def test_landing_success(client, assertStatusCode2xx):
    response = client.get('/')
    assert b'<title>Landing</title>' in response.data
    assertStatusCode2xx(response.status_code)  

def test_login_success(client, assertStatusCode2xx):
    response = client.get('/login')
    assert b'<title>Login</title>' in response.data
    assertStatusCode2xx(response.status_code)

def test_signup_success(client, assertStatusCode2xx):
    response = client.get('/signup')
    assert b'<title>Signup</title>' in response.data
    assertStatusCode2xx(response.status_code) 

def test_generate_loggedin(client, assertStatusCode2xx):
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    response = client.get('/gen', follow_redirects=True)
    assert b'<title>Generate</title>' in response.data
    assertStatusCode2xx(response.status_code) 