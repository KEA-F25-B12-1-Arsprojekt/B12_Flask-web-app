# imports
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from sqlscripts import handle_employee_check_in, get_employee_record
import sqlite3


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "3415a2ef17b0f9ebe00f0a7b08d07e64122ca753427e4ece0d8c46d729d8c536" # Change later (make random?)

db = SQLAlchemy(app)
db_path = "user_time.db"
login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app routing and run
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html", form = form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

@app.route('/dashboard')
@login_required
def dashboard():
    emp_id = current_user.username
    record = get_employee_record(emp_id)  # Fetch user’s check-in record

    user_checked_in = False
    if record:
        current_login = record[2]  # LOGIN column
        current_logout = record[3]  # LOGOUT column
        if current_login != 'empty' and current_logout == 'empty':
            user_checked_in = True  # User is currently checked in
    
    # Connect to SQLite database using correct DB path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all employees who are checked in (LOGOUT is still 'empty') along with their login times & dates
    query = "SELECT ID, DATE, LOGIN FROM EMPLOYEE_TIME WHERE LOGOUT = 'empty'"
    cursor.execute(query)
    checked_in_users = cursor.fetchall()  # List of tuples (ID, DATE, LOGIN)

    conn.close()
    
    return render_template('dashboard.html', user_checked_in=user_checked_in, checked_in_users=checked_in_users)

@app.route("/signup", methods = ["GET", "POST"])
@login_required
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username = form.username.data, firstname = form.firstname.data, lastname = form.lastname.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", form = form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/check-in-out", methods=["POST"])
@login_required
def check_in_out():
    emp_id = current_user.username  # Get logged-in user's ID
    handle_employee_check_in(emp_id)  # Only pass emp_id, let class.py handle timestamps

    flash("Check-in/out recorded successfully!", "success")
    return redirect(url_for("dashboard"))


app.run(debug=True)
2