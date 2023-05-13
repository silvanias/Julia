def login(client):
    client.post('/signup', data={
    'username':'test', 
    'email':'user@test.com',
    'password1':'password',
    'password2':'password'
    })

def mandelbrot_winput(client):
    client.post('/gen', data={
        'hexval':'FFFFFF',
        'sets':'mandelbrot'
        })