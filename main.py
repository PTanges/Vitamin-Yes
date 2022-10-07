# Import the Flask framework
from flask import Flask

# Create an app that hosts the application so that you can use decorators (don't worry about this for now)
app = Flask(__name__)

# Route a Python function to the root URL
@app.route('/')
def index():
    # Return something to display in the browser. This can be HTML, but let's start basic
    textOutput = "Vitamin A is the name of a group of fat-soluble retinoids, primarily retinol and retinyl esters\n. Vitamin A is involved in immune function, cellular communication, growth and development,\nand male and female reproduction. Vitamin A supports cell growth and differentiation,\nplaying a critical role in the normal formation and maintenance of the heart, lungs, eyes,\nand other organs. Vitamin A is also critical for vision as an essential component of rhodopsin,\nthe light-sensitive protein in the retina that responds to light entering the eye, and because\nit supports the normal differentiation and functioning of the conjunctival membranes and cornea..."
    return textOutput

# Start the server
app.run(threaded=True, port=5000)
