from pymongo import MongoClient
import datetime
import jwt
from mytrip.src.model import validate
from mytrip.src.model import services

client = MongoClient()
client = MongoClient('localhost', 27017) #mongo_db uses local host to store data
db = client['GetMyTrip']
user_collection = db['user']
pialot_collection = db['pilot']

class user:

    def __init__(self):
        pass

    def save(details):
        try:
            user_details_to_save = dict()
            if (validate.user.signup(details) == True):
                if(user.is_user_exist("email", details["email"] == True)):
                    return "user_email_exist"
                if(user.is_user_exist("phone", details["phone"]== True)):
                    return "user_phone_exist"
                user_details_to_save = dict(details)
                current_pswd = details["pwd"]
                key =  "jwt" #change the logic for key
                encrypt_pswd = jwt.encode({"pwd" : current_pswd}, key, algorithm = 'HS256') #encryption
                user_details_to_save["pwd"] = encrypt_pswd
                user_details_to_save["creation_data"] = datetime.datetime.utcnow()
                user_details_to_save["password_expiry_data"] = datetime.datetime.today()+datetime.timedelta(days=120)
                user_details_to_save["status"] = "inactive"
                user_details_to_save["is_phone_verified"] = False
                user_details_to_save["is_email_verified"] = False
                user_details_to_save["status"] = "inactive"
                user_details_to_save["is_deleted"] = False
                user_collection.insert_one(user_details_to_save) #save user to db
                return True  
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def is_user_exist(id_type, id, pswd = None):
        try:
            key =  "jwt" #change the logic for key
            user_details_from_db = user_collection.find_one({id_type:str(id)})
            
            if(user_details_from_db == None):
                return False 
            elif(user_details_from_db["status"] == "active" and 
                user_details_from_db["is_deleted"] == False):
                return True
            elif(pswd and 
               user_details_from_db["status"] == "active" and
               user_details_from_db["is_deleted"] == False):
                m_decrypt = jwt.decode(user_details_from_db["pwd"], key, algorithms=['HS256'])
                if(pswd == m_decrypt["pwd"]):
                    return True
                else:
                    pass
            elif(user_details_from_db["status"] == "inactive" and
                 user_details_to_save["is_phone_verified"] == False and
                 user_details_to_save["is_email_verified"] == False):
                   return "verification_required"

        except Exception as e:
            print(e)
            return False

    def login(details):
        try:
            details = validate.user.login(details)
            print(details)
            if(user.is_user_exist(details[0], details[1], details[2]) == True):
                return True
            else:
                return False   
        except Exception as e:
            print(e)
            return False

    def send_validation_code():
        try:
            email_code = validate.generate.code()
            phone_code = validate.generate.code()
            if(services.sms.sendsms(details["phone"], phone_code) == True and
              services.smtp.sendmail(details["phone"], email_code) == True):
                return (phone_code, email_code)
        except Exception as e:
            print(e)
            return False

    def check_to_validate(id_type, id):
        try:
            user_details_from_db = user_collection.find_one({id_type:str(id)})
            if(user_details_from_db["status"] == "inactive" and 
                    user_details_from_db["is_deleted"] == False):
                    return True  
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def send_validation_code(validation_details):
         if(user.check_to_validate("email", validation_details["email"] == True) and
            user.check_to_validate("phone", validation_details["phone"] == True)):
             if(services.sms.send_sms( validation_details["phone"], "otp") == True and 
                services.email.send_email(validation_details["email"], "test", "otp") == True):
                return True

    

