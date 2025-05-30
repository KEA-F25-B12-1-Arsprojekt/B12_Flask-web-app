#Set-up for the User class model for Flask-login, used to create the database users.db
#imports
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)