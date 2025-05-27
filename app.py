# imports
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


# app routing and run
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)
2