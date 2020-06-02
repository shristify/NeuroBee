from django.shortcuts import render
import pyrebase
from django.contrib import auth
import json
import requests as msgRequest
import time
from django import urls as urlresolvers
try:
    from django.urls.exceptions import NoReverseMatch
except ImportError:
    from django.core.urlresolvers import NoReverseMatch

config={
  'apiKey': "AIzaSyCUchbdcHU75ahgwcyOnqqLupMauIbR32I",
  'authDomain': "friendlychat-ssss.firebaseapp.com",
  'databaseURL': "https://friendlychat-ssss.firebaseio.com",
  'projectId': "friendlychat-ssss",
  'storageBucket': "friendlychat-ssss.appspot.com",
  'messagingSenderId': "338120484312",
  'appId': "1:338120484312:web:a6432d15c2b2bdf0563ead",
  'measurementId': "G-R0WLSHM6D0"
}
#   // Initialize Firebase
firebase=pyrebase.initialize_app(config)

auths=firebase.auth()
database=firebase.database()

def intro(requests):
    return render(requests, "homePage.html")

def signIn(requests):
    return render(requests, "login.html")

  
def postsign(requests):
    email=requests.POST.get('email')
    passw=requests.POST.get('pass')
    try:
      user=auths.sign_in_with_email_and_password(email,passw)
      session_id=user['idToken']
      requests.session['uid']=str(session_id)
    except:
        message="invalid credentials"
        return render(requests,"login.html",{"messg":message})
    print(user['idToken'])
    return render(requests,'mainPage.html',{"e":email})
    
def quiz(requests):
    if requests.session['uid']==str(session_id):
     return render(requests,'index.html')
    return render(requests,"login.html")

def you(requests):
    if requests.session['uid']==str(session_id):
      return render(requests,'you.html')
    return render(requests,"login.html")
   

def waterReminder(requests):
    t=time.time()+ 30*60
    print(t)

    message="Time to drink Water"    
    while(True):
        if(time.time==t):
            return render(requests, 'mainPage.html', {'msg':message})
            

    return render(requests,'mainPage.html')    

    
    






def logout(requests):
    auth.logout(requests)
    del requests.session['uid']
    msg="sucessfully logged out"
    return render(requests,"homePage.html",{"messg":msg})    

def signUp(requests):
    return render(requests,"signup.html")   


def postsignUp(requests):
 email=requests.POST.get('email')
 passw=requests.POST.get('pass')
 name=requests.POST.get('Fname')
 friend1no=requests.POST.get('friend1no')
 friend2no=requests.POST.get('friend2no')

 user=auths.create_user_with_email_and_password(email,passw)
 uid=user['localId']

 data= {"name":name, "status":"1", "friend1no":friend1no,"friend2no":friend2no}

 database.child(uid).child("details").set(data)
 msg="Account created sucessfully, please login now"
 return render(requests,"login.html",{"messg":msg})



def sendsms(requests):
     url='https://www.fast2sms.com/dev/bulk'

     idtoken=requests.session['uid'] 
     a=auths.get_account_info(idtoken)
     a =a['users']
     print(a)
     a =a[0]
     a =a['localId']
     print(a)

     name=database.child(a).child('details').child('name').get().val()
     firstFriendNumber=database.child(a).child('details').child('friend1no').get().val()
     

     print(firstFriendNumber)
     print(name)
     para={
         'authorization':'XYmpiL3FWBhEcz50HxVuQDteI1RlUgojsSqCO2rGdwyMTvb9PkfaP6NUeFHvVAzjwTnXydOrkEKmo1Gt',
         'sender_id':"FSTSMS",
         'message':"your friend needs your help, plz contact him",
         'language':'english',
         "route":"p",
         'numbers':firstFriendNumber
         
     }   
    

     response=msgRequest.get(url, params=para)
     print(response.json())
     msg="message sent successfully"
     return render(requests,"mainPage.html",{"messg":msg})


def DocsNear(requests):
  return render(requests, 'mapsFinal.html')




