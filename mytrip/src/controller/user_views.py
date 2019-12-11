from datetime import datetime
from flask import render_template
from mytrip import app

@app.route('/user')
def user():
    return "user page"

@app.route('/user/login')
def user_login():
    return "user login"

@app.route('/user/signup')
def user_signup():
    return "user signup"