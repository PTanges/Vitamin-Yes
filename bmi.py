from flask import Flask, render_template

app = Flask(__name__)

@app.route("/BMI", methods=('GET', 'POST'))
def bmi():
    return render_template("BMI.html")