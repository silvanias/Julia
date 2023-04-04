from juliaapp.extensions.database import db, CRUDMixin
from sqlalchemy.sql import func
from sqlalchemy import Enum
import enum
from flask_login import UserMixin
class User(db.Model, CRUDMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    creation_date = db.Column(db.DateTime(timezone = True), default = func.now())
    fractals = db.relationship('Fractal', backref='user', lazy=True)

class MyEnum(enum.Enum):
    mandel = 1
    julia = 2    

class Fractal(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    fractal_type = db.Column(Enum(MyEnum))
    hex_value = db.Column(db.Integer, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)