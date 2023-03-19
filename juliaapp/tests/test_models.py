from juliaapp.extensions.database import db
from juliaapp.models import User
from datetime import datetime

def test_save_person(client):
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
