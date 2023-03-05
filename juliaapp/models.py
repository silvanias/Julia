from juliaapp.extensions.database import db, CRUDMixin
from sqlalchemy.sql import func
from flask_login import UserMixin
class User(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    creation_date = db.Column(db.DateTime(timezone = True), default = func.now())