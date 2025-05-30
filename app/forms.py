# Flask WT Forms setup for registering a user, and logging in a user
# Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired(), Length(min = 4, max = 20)])
    password = PasswordField("Password", validators = [DataRequired(), Length(min = 6, max = 20)])
    firstname = StringField("First name", validators = [DataRequired()])
    lastname = StringField("Last name", validators = [DataRequired()])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("Login")