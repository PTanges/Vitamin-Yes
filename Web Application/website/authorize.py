from flask import Blueprint, request, render_template, flash

authorize = Blueprint("routes", __name__)

@authorize.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html", boolean = True)

@authorize.route("/create_account", methods = ["GET", "POST"])
def create_account():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        domain = (".net", ".com", ".org", ".gov", ".edu")
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif not email.endswith(domain):
            flash("Email must end with a top-level domain", category="error")
        elif len(firstName) < 2:
            flash("First Name is too short", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            flash("Account created successfully", category="success")
            # add user to database

    return render_template("create_account.html", boolean = True)

@authorize.route("/sign_out")
def sign_out():
    return "<p>You've signed out!</p>"
# May later replace this with a simple redirect to Login page