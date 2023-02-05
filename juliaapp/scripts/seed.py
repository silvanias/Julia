from juliaapp.app import create_app
from juliaapp.models import User
from juliaapp.extensions.database import db

app = create_app()
app.app_context().push()

users_data = {
    "admin" : {"email": "test@test.com", "password": "password"}
}

for user, data in users_data.items():
    new_user = User(username=user, email=data['email'], password=data['password'])
    db.session.add(new_user)

db.session.commit()