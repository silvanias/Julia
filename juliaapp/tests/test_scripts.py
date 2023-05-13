def login(client):
    client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })