# imports
from flask import Flask, render_template

app = Flask(__name__)

# app routing and run
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def about():
    return render_template('login.html')

app.run(debug=True)
2