from pymongo import MongoClient
import datetime
import jwt
from mytrip.src.model import validate


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
            if validate.user.signup(details) == True :
                user_details_to_save = dict(details)
                current_pswd = details["pwd"]
                key =  "jwt" #change the logic for key
                encrypt_pswd = jwt.encode({"pwd" : current_pswd}, key, algorithm = 'HS256') #encryption
                details["pwd"] = encrypt_pswd
                details["creation_data"] = datetime.datetime.utcnow()
                details["password_expiry_data"] = datetime.datetime.today()+datetime.timedelta(days=120)
                details["status"] = "active"
                details["is_deleted"] = False
                user_collection.insert_one(details) #save user to db
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
            if(pswd and 
               user_details_from_db["status"] == "active" and
               user_details_from_db["is_deleted"] == False):
                m_decrypt = jwt.decode(user_details_from_db["pwd"], key, algorithms=['HS256'])
                if(pswd == m_decrypt["pwd"]):
                    return True
                else:
                    return False
            elif(user_details_from_db == None):
                    return False 
            elif(user_details_from_db["status"] == "active" and 
                 user_details_from_db["is_deleted"] == False):
                return True        
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

