# from package import db, otherwise would be from website import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Import Custom Class to help define table schema
# All User data must conform to schema defined below
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(25))
    first_name = db.Column(db.String(20))

    # List that will store all of the user's generated assessments
    # One to many
    assessment = db.relationship("Assessment")

# TO DO: Create schema to store health information & Connect that table to User
'''
Note for future staff engineers:
You must always have a primary key (unique value, names are not unique values) per table
and be sure to separate your table values. Store sleep data separately from the Health
'''

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Appends the current date and time via func.now(), may be useful when generating user health assessments
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    # The integer value is the maximum amount of characters
    synopsis = db.Column(db.String(10000))

    # As per SQL standards, relate User to Assessment via Foreign Key
    # One to many relationship
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))