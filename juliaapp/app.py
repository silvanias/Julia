from flask import Flask
from juliaapp.extensions.database import db 
from . import routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('juliaapp.config')
    register_extensions(app)
    register_blueprints(app)
    
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)