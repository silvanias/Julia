# SCRIPT IS CURRENTLY A ONE TIME USE (CANNOT SUBMIT DUPLICATE VALUES)
from juliaapp.app import create_app
from juliaapp.models import User
from juliaapp.extensions.database import db
from datetime import datetime

app = create_app()
app.app_context().push()

temp_creation_date = datetime(2023, 2, 10, 12, 00, 00)
users_data = {
    "vani" : {"email": "vani@gmail.com", "password": "vainguy", "creation_date": temp_creation_date}
}

for user, data in users_data.items():
    new_user = User(username=user, email=data['email'], password=data['password'], creation_date=data['creation_date'])
    db.session.add(new_user)
    
db.session.commit()