def test_signup_content(client):
    # Returns landing content
    response = client.get('/signup')
    assert b'<input type="text" name="username" id="username" placeholder="Username" required>' in response.data
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password1" id="password1" placeholder="Password" required>' in response.data
    assert b'<input type="password" name="password2" id="password2" placeholder="Confirm Password" required>' in response.data 

def test_login_content(client):
    # Returns landing content
    response = client.get('/login')
    assert b'<input type="email" name="email" id="email" placeholder="Email" required>' in response.data
    assert b'<input type="password" name="password" id="password" placeholder="Password" required>' in response.data  

## LEARN HOW TO DO WITH MOCKING
def test_generate_loggedin(client, assertStatusCode2xx):
    response = client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })
    response = client.get('/gen', follow_redirects=True)
    assert b'<title>Generate</title>' in response.data
    assert b'<input type="number" name="realnum" id="realnum" placeholder="Real Number">' in response.data
    assert b'<input type="number" name="imagnum" id="imagnum" placeholder="Imaginary Number">' in response.data
    assert b'<input type="text" name="hexval" id="hexval" placeholder="Hex value (RRGGBB)" aria-required="true">' in response.data
    assert b'<button type="submit" class="input-button"> Generate </button>' in response.data
    assertStatusCode2xx(response.status_code) 