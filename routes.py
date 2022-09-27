from flask import Blueprint, render_template

routes = Blueprint(__name__, "route")

@routes.route("/")
def home():
    return "Welcome to Vitamin-Yes"

@routes.route("/Vitamin-C")
def vitaminC():
    return render_template("vitamin-C.html", studentName="Patrick Wong")

@routes.route("/Vitamin-D")
def vitaminD():
    return render_template("vitamin-D.html", studentName="Patton Tang")