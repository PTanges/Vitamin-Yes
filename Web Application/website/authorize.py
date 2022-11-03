from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_remembered, logout_user, current_user, login_required

authorize = Blueprint("routes", __name__)

@authorize.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Returns first result of a value that matches query
        user = User.query.filter_by(email=email).first()
        if user:
            # Compare incoming password against database password
            if check_password_hash(user.password, password):
                flash("Login successful!", category="success")
                login_user(user, remember=True)
            else:
                flash("Incorrect password, try again", category="error")
        else:
            # else is when no email is found, ie no user exists
            # currently we only allow ONE account per email under this schema
            flash('Email does not exist.', category="error")

    return render_template("login.html", user=current_user)

@authorize.route("/sign_out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('routes.login'))

@authorize.route("/create_account", methods = ["GET", "POST"])
def create_account():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # May rework the if elif structure to be part of the try except, manually raising an error with raise ValueError etc
        try:
            # Will accept alpha-numeric characters
            email = email.upper()
            first_name = first_name.upper()
        except:
            pass

        # Most Common Top Level Domains
        domain = (".NET", ".COM", ".ORG", ".GOV", ".EDU", ".BLOG", ".UK", ".US", ".DE", ".IO", ".CO", ".BIZ", ".XYZ")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif not email.endswith(domain):
            flash("Email must end with a top-level domain", category="error")
        elif len(first_name) < 2:
            flash("First Name is too short", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            # Common hashing algorithms are MD5, SHA-1, SHA-2, NTLM, LANMAN, Sha256 chosen arbitrarily as of now
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            # Flash may be unnecessary due to the redirect
            flash('Account created!', category="success")
            return redirect(url_for("route.home"))

    return render_template("create_account.html", user=current_user)