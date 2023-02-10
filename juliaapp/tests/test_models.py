from juliaapp.extensions.database import db
from juliaapp.models import User
from datetime import datetime

def test_user_update(client):
    temp_creation_date = datetime(2000, 1, 1, 12, 00, 00)
    user = User(username='test', email='usertestemail@test.com', password='password', creation_date=temp_creation_date)
    db.session.add(user)
    db.session.commit()

    user.password = 'changedpassword'
    user.save()

    updated_user = User.query.filter_by(username='test').first()
    assert updated_user.password == 'changedpassword'

def test_user_delete(client):
    temp_creation_date = datetime(2000, 1, 1, 12, 00, 00)
    user = User(username='test', email='usertestemail@test.com', password='password', creation_date=temp_creation_date)
    db.session.add(user)
    db.session.commit()

    user.delete()

    deleted_user = User.query.filter_by(username='test').first()
    assert deleted_user is None
