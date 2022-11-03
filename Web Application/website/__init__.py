from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# SQL Database
db = SQLAlchemy()
DATABASE_MASTER = "database.db"


def create_application():
    # Create an app that hosts the application so that you can use decorators
    app = Flask(__name__)

    # Basic encryption and prevent cookies from being stolen
    app.config['SECRET_KEY'] = 'Y$gH3xe2c4YbnD0iD*^UfN6KlDNY9b'

    # Direct Files to find database inside Website Folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_MASTER}'

    # Initialize and run init, will treat folder as a package
    db.init_app(app)

    # Routing and Connecting
    from .routes import routes
    from .authorize import authorize
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(authorize, url_prefix="/")

    from .models import User

    # Import table schemas, must run and load models.py before initialize DB
    # Dot operator makes this a relative import
    # No need to check for prior existing DB, flask will check
    from . import models
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app