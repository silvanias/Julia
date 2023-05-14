from juliaapp.models import User, Fractal
from datetime import datetime

def test_save_user(client):
    user = User(username='test', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user.save()

    users = User.query.filter_by(username='test').all()
    assert len(users) == 1

def test_user_update(client):
    user = User(username='test', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user.save()

    user.password = 'changedpassword'
    user.save()

    updated_user = User.query.filter_by(username='test').first()
    assert updated_user.password == 'changedpassword'

def test_user_delete(client):
    user = User(username='test', email='user@test.com', password='password', creation_date=datetime(2000, 1, 1, 12, 00, 00))
    user.save()

    user.delete()
    deleted_user = User.query.filter_by(username='test').first()
    assert deleted_user is None

def test_save_frac(client):
    frac = Fractal(fractal_type='mandelbrot',hex_value='FFFFFF',user_id=1)
    frac.save()
    fracs = Fractal.query.filter_by(hex_value='FFFFFF').all()
    assert len(fracs) == 1

def test_frac_delete(client):
    frac = Fractal(fractal_type='mandelbrot',hex_value='FFFFFF',user_id=1).save()
    
    frac.delete()
    deleted_frac = Fractal.query.filter_by(hex_value='FFFFFF').first()
    assert deleted_frac is None
