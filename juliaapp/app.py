from flask import Flask
from juliaapp.extensions.database import db, migrate 
from . import routes
from juliaapp.extensions.authentication import login_manager
from juliaapp.config import Config

def create_app(config: Config = Config()):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    
    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    app.register_blueprint(routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)