import requests
from mytrip import config

class sms:
    def send_sms(phone, message):
        url = config.dev.sms_url
        querystring = {"method":"sms","sender":"BRANDS","to":phone,"message":message,"api_key":config.dev.sms_key}
        response = requests.request("GET", url, params=querystring)
        print(response.text)
    