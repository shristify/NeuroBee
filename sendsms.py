import requests
import json


def send_sms(number,message):
    url='https://www.fast2sms.com/dev/bulk'


    para ={
        'authorization':'XYmpiL3FWBhEcz50HxVuQDteI1RlUgojsSqCO2rGdwyMTvb9PkfaP6NUeFHvVAzjwTnXydOrkEKmo1Gt',
        'sender_id':"FSTSMS",
        'message': message,
        'language':'english',
         "route":"p",
        'numbers':number

    }

    response=requests.get(url,params=para)
    print(response.json())



send_sms(7770878986,"hello prajjwal this is sent using python")