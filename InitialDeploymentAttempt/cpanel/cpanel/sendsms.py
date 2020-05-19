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

#def sendsms(requests):
#     url='https://www.fast2sms.com/dev/bulk'

#     idtoken=requests.session['uid'] 
#     a=auths.get_account_info(idtoken)
#     a =a['users']
#     a =a[0]
#     a =a['localId']

#     name=database.child('users').child(a).child('details').child('name').get().val()
#     friend1no=database.child('users').child(a).child('details').child('friend1no').get().val()
#     friend2no=database.child('users').child(a).child('details').child('friend2no').get().val()
#     para={
#         'authorization':'XYmpiL3FWBhEcz50HxVuQDteI1RlUgojsSqCO2rGdwyMTvb9PkfaP6NUeFHvVAzjwTnXydOrkEKmo1Gt',
#         'sender_id':"FSTSMS",
#         'message': "your friend  needs your help, plz contact him",
#         'language':'english',
#         "route":"p",
#         'numbers':friend1no
#     }   
    

#     response=requests.POST.get(url, params=para)
#     print(response.json())
#     msg="message sent successfully"
#     return render(requests,"page3.html",{"messg":msg})
