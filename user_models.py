from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)  # Add this if missing
    lastname = db.Column(db.String(100), nullable=False)   # Add this if missing
    password = db.Column(db.String(100), nullable=False)