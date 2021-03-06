from datetime import datetime
from mytrip import app
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask_api import status
from mytrip.src.service import db

#pip freeze

@app.route('/user')
def user():
    login = False
    if(login):
        return user_profile
    else:
       return display_user_login()

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
    signup_details = request.form
    if db.user.save(signup_details) == True:
        response_object = {
                            'status': 'success',
                            'message': 'User Successfully Registered please verify to activate.'
                              }
        print("success: user successfully added to db")
        return ('verify.html',
                            title='Verification Page',
                            year=datetime.now().year)
    else:
        response_object = {
                            'status': 'failed',
                            'message': 'invalid Details'
                                }
        print("error: Invalid user details to register")
        return response_object, status.HTTP_203_NON_AUTHORITATIVE_INFORMATION

@app.route('/user')
def user_profile():
    return render_template(
                            'user.html',
                            name = "Sasi",
                            title='User Profile',
                            year=datetime.now().year)

@app.route('/book/ride')
def book_ride():
    return render_template(
                            'Ride.html',
                            title='Booking a Ride',
                            year=datetime.now().year
                            )
@app.route('/maps')
def maps():
    return render_template(
                            'maps.html',
                            title='maps',
                            year=datetime.now().year
                            )

@app.route('/user/verify', methods = ["POST"])
def post_validate():
    #signup_details = request.form
    validation_details = request.form
    if(validation_details["pcode"] == "0000" and validation_details["ecode"] == "0000"):
        response_object = {
                            'status': 'success',
                            'message': 'User Successfully verified to activate.'
                              }
        print("success: user successfully added to db")
        return response_object, status.HTTP_200_OK

@app.route('/user/verify')
def get_verify():
    return render_template(
                            'verify.html',
                            title='verify',
                            year=datetime.now().year
                            )

   
        

