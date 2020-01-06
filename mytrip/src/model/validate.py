import datetime
import re
import random 
import jwt


class user:

    def __init__(self):
        pass

    def name(string):
        """ Validates the string have name """
        Number = user.check_int(string)
        if(len(string) > 3 and string.isalpha()):
            return True
        else:
            return False

    def emailid(email):
        """ Validates the email """
        email_formate = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if(re.search(email_formate, email)):
            return True
        else:
            return False

    def pswd(password):
        """ Validate password """
        capsalpha = smallalpha = num = splchar = False
        for _ in password:
            if(_ >= 'A' and _ <= 'Z'): 
                capsalpha = True
            elif(_ >= 'a' and _ <= 'z'):
                smallalpha = True
            elif(_ >= '0' and _ <= '9'):
                num = True
            else:
                splchar = True
        #password should contain caps, small, number and special char
        if(capsalpha and smallalpha and num and splchar):  
            return True
        else:
            return False

    def phone_number(phone):
        """ Validates the Phone number """
        phone = str(phone)
        if(len(phone) == 10 and phone[0] in "6789" and user.check_int(phone)):
            #number should be 10 digits and start with 6 or 7 or 8 or 9
            return True
        else:
            return False

    def check_int(number):
        """ Validates given data is int or not """
        try:
            number = int(number)
            return True
        except:
            return False

    def signup(details):
        try:
            if(user.emailid(details["email"]) and user.pswd(details["pwd"]) and
               user.name(details["name"]) and user.phone_number(details["phone"])):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def login(details):
        try:
            id = details["id"]
            password = details["pwd"]
            #check given id is phone number or email
            if(user.check_int(id) == True):
                return("phone", id, password)
            else:
                return("email", id, password)
        except Exception as e:
            print(e)
            return False

class generate:
    def code():
        ramdom_value = random.randint(0,99999)
        return ramdom_value
