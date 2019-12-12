from datetime import datetime
from mytrip import app
from flask import render_template
from flask import request
from flask import jsonify
from flask_api import status
from mytrip.src.service import db

#pip freeze

@app.route('/user')
def user():
    return "user page"

@app.route('/user/login')
def display_user_login():
    return render_template(
        'user_login.html',
        title='Login Page',
        year=datetime.now().year)

@app.route('/user/login', methods = ["POST"])
def user_login():
    login_details = request.get_json()
    if db.user.login(login_details) == True:
        response_object = {
                            'status': 'success',
                            'message': 'User Successfully Logged in.'
                              }
        print("success: user successfully loggedin to application")
        return response_object, status.HTTP_200_OK
    else:
        response_object = {
                            'status': 'failed',
                            'message': 'invalid Details'
                                }
        print("error: Invalid user details to Login")
        return response_object, status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

@app.route('/user/signup')
def display_user_signup_page():
    return render_template(
        'user_signup.html',
        title='Signup Page',
        year=datetime.now().year)

@app.route('/user/signup', methods = ["POST"])
def save_user_signup():
    #signup_details = request.form
    signup_details = request.get_json()
    if db.user.save(signup_details) == True:
        response_object = {
                            'status': 'success',
                            'message': 'User Successfully Registered.'
                              }
        print("success: user successfully added to db")
        return response_object, status.HTTP_200_OK
    else:
        response_object = {
                            'status': 'failed',
                            'message': 'invalid Details'
                                }
        print("error: Invalid user details to register")
        return response_object, status.HTTP_203_NON_AUTHORITATIVE_INFORMATION


