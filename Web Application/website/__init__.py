from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

    # Initialize
    DATABASE_MASTER.__init__(app)


    # Routing and Connecting
    from .routes import routes
    from .authorize import authorize
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(authorize, url_prefix="/")

    return app