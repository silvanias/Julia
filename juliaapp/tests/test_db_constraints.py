from juliaapp.models import User, Fractal
from datetime import datetime
from sqlalchemy.exc import IntegrityError

def test_user_constraint(client):
    user1 = User(username='test', email='user1@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user1.save()

    user2 = User(username='test', email='user2@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    try:
        user2.save()
    except IntegrityError:
        assert True

def test_email_constraint(client):
    user1 = User(username='test1', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user1.save()

    user2 = User(username='test2', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    try:
        user2.save()
    except IntegrityError:
        assert True

def test_fractal_nouser_constraint(client):
    frac = Fractal(fractal_type='mandelbrot',hex_value='FFFFFF',user_id=None)
    try:
        frac.save()
    except IntegrityError:
        assert True

def test_user_with_fractal_delete_constraint(client):
    user1 = User(username='test', email='user1@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user1.save()
    frac = Fractal(fractal_type='mandelbrot',hex_value='FFFFFF',user_id=1)
    frac.save()
    try:
        user1.delete()
    except IntegrityError:
        assert True