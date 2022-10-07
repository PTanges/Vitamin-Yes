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

@routes.route("/BMI", methods=('GET', 'POST'))
def bmi():
    return render_template("BMI.html")

@routes.route("/Vitamin-E")
def vitaminE():
    return render_template("Vitamin-E.html", studentName="Alejandro Ramos")
    
@routes.route("/Vitamin-K")
def vitaminK():
    return render_template("Vitamin-K.html", studentName="Alejandro Ramos")
   
@routes.route("/Iron")
def Iron():
    return render_template("Iron.html", studentName="Alejandro Ramos")
   
@routes.route("/Calcium")
def Calcium():
    return render_template("Calcium.html", studentName="Alejandro Ramos")
   
@routes.route("/FolicAcid")
def FolicAcid():
    return render_template("FolicAcid.html", studentName="Alejandro Ramos")
    
@routes.route("/Iodine")
def Iodine():
    return render_template("Iodine.html", studentName="Alejandro Ramos")

@routes.route("/Magnesium")
def Magnesium():
    return render_template("Magnesium.html", studentName="Alejandro Ramos")
