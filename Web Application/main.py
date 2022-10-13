# Import the Flask framework
from website import create_application

# Initialize Application
app = create_application()

# Start the server
if __name__ == "__main__":
    app.run(debug = True, port=5000)