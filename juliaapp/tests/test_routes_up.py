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

# Temporarily broken, make sure to add two different checks, one for logged in users and not logged in users
def test_generate_success(client, assertStatusCode2xx):
    response = client.get('/gen')
    assert b'<title>Generate</title>' in response.data
    assertStatusCode2xx(response.status_code) 