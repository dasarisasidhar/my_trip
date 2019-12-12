from datetime import datetime
from flask import render_template
from mytrip import app

@app.route('/user')
def user():
    return "user page"

@app.route('/user/login')
def user_login():
    return render_template(
        'user_login.html')

@app.route('/user/signup', methods = ["GET","POST"])
def user_signup():
    return render_template(
        'user_signup.html')
    if(methods == "POST"):
        pass