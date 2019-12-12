from datetime import datetime
from flask import render_template
from mytrip import app

@app.route('/pilot')
def pilot():
    return "pilot page"

@app.route('/pilot/login')
def pilot_login():
    return render_template(
        'pilot_login.html')

@app.route('/pilot/signup')
def pilot_signup():
    return render_template(
        'pilot_signup.html')

