from flask import Flask

def create_application():
    # Create an app that hosts the application so that you can use decorators
    app = Flask(__name__)

    # Basic encryption and prevent cookies from being stolen
    app.config['SECRET_KEY'] = 'Y$gH3xe2c4YbnD0iD*^UfN6KlDNY9b'

    from .routes import routes
    from .authorize import authorize
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(authorize, url_prefix="/")

    return app