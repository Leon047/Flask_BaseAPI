from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize the app with the extension
    db.init_app(app)

    # Initialize marshmallow
    ma.init_app(app)

    # Initialize api
    global api
    api = Api(app)

    with app.app_context():
        from .views import HelloWorld

        # Create Database Models
        db.create_all()

        # App Routes
        api.add_resource(HelloWorld, '/api/v1.0/hello')

        return app
