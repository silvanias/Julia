from flask import Flask
from . import routes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('instance.config')

    register_blueprints(app)
    
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(routes.blueprint)