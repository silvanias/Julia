from juliaapp.tests.scripts_for_testing import login

def test_signup_content(client, assertStatusCode2xx):
    # Returns landing content
    response = client.get('/signup')
    assert b'<input type="text" name="username" id="username" placeholder="Username" required>' in response.data
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password1" id="password1" placeholder="Password" required>' in response.data
    assert b'<input type="password" name="password2" id="password2" placeholder="Confirm Password" required>' in response.data 
    assertStatusCode2xx(response.status_code)
    
def test_login_content(client, assertStatusCode2xx):
    # Returns landing content
    response = client.get('/login')
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password" id="password" placeholder="Password" required>' in response.data  
    assertStatusCode2xx(response.status_code)

from unittest.mock import PropertyMock, patch
from juliaapp.models import User
from datetime import datetime 
def test_generate_content(client, assertStatusCode2xx):
    # Mock current_user
    user1 = User(username='test1', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    with patch('flask_login.utils._get_user', new_callable=PropertyMock) as get_user:
        get_user.return_value = user1
        response = client.get('/gen', follow_redirects=True)
        assert b'<title>Generate</title>' in response.data
        assert b'<input type="number" name="realnum" id="realnum" placeholder="Real Number">' in response.data
        assert b'<input type="number" name="imagnum" id="imagnum" placeholder="Imaginary Number">' in response.data
        assert b'<input type="text" name="hexval" id="hexval" placeholder="Hex value (RRGGBB)" aria-required="true">' in response.data
        assert b'<button type="submit" class="input-button"> Generate </button>' in response.data
        assertStatusCode2xx(response.status_code) 

def test_landing_content(client, assertStatusCode2xx):
    response = client.get('/')
    assert b'<title>Landing</title>' in response.data
    assert b'<p>PLEASE DO NOT SUBMIT ANY PERSONAL DATA TO THIS WEBSITE, IT IS PURELY A TECHNICAL EXPERIMENT!</p>' in response.data
    assertStatusCode2xx(response.status_code) 