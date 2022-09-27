# Import the Flask framework
from flask import Flask
from routes import routes

# Create an app that hosts the application so that you can use decorators
app = Flask(__name__)
app.register_blueprint(routes, url_prefix="/")

# Start the server
if __name__ == "__main__":
    app.run(debug = True, port=5000)
    # app.run(threaded=True, port=5000)