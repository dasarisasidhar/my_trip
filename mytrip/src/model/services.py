import requests
import smtplib
import config


key = config.dev.sms_key()
url = config.dev.sms_url()
_email = config.dev.smtp_id()
password = config.dev.smtp_password()

class sms:
    def __init__():
        pass

    def send_sms(phone, Type):
        if(type == "otp"):
            message =  "0000"
        querystring = {"method":"sms","sender":"BRANDS","to":phone,"message":message,"api_key":key}
        response = requests.request("GET", url, params=querystring)
        print(response.text)
        return message

class email:
    def __init__():
        pass

    def send_email(email, name , type):
        """
        details contains tuple of elements
        input: name of user, emailid, type (of message eg: signup)
        output: sends email
        """
        _email = "" #source from mail will send
        message = ""
        
        if(type == "signup"):
            # details[0] is user_mail_id and  details[1] is name and details[2] is code
            message = f"""
            Welcome {name}, 
            Thankyou for signingup to our Book Store Application. Hope you will get better experience with us.
            "YOUR CODE IS {validation_code}"
            Regards,
            Flaskbackend Application Team
            """
        elif(type == "otp"):
            message = "0000"

        else: message = """
                Test email
                """
        try:
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login(_email, password)
            mail.sendmail(_email, email, message)
            mail.close()
            return True

        except:
            return "exception: sending mail"