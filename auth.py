from flask import Blueprint, render_template
...
@auth.route('/login')
def login():
    return render_template('login.html')
