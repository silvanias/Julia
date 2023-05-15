from juliaapp.models import User
from unittest.mock import PropertyMock, patch
from datetime import datetime 

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

def test_generate_restricted(client, assertStatusCode2xx):
    response = client.get('/gen', follow_redirects=True)
    
    assert b'<title>Login</title>' in response.data
    assertStatusCode2xx(response.status_code) 
    
def test_generator_success(client, assertStatusCode2xx):
    # Mock locked in user    
    user1 = User(username='test1', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    with patch('flask_login.utils._get_user', new_callable=PropertyMock) as get_user:
        get_user.return_value = user1
        response = client.get('/gen', follow_redirects=True)

        assert b'<title>Generate</title>' in response.data
        assertStatusCode2xx(response.status_code)