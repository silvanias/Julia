def test_landing_success(client):
    # Page loads
    response = client.get('/')
    assert response.status_code == 200

def test_login_success(client):
    # Page loads
    response = client.get('/login')
    assert response.status_code == 200

def test_signup_success(client):
    # Page loads
    response = client.get('/signup')
    assert response.status_code == 200

def test_generate_success(client):
    # Page loads
    response = client.get('/gen')
    assert response.status_code == 200