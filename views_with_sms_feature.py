from django.shortcuts import render
import pyrebase
from django.contrib import auth
import json
import requests as msgRequest

config={

    # this is for my project of neuro chat, isko change kar lena 
    'apiKey': "AIzaSyDca9qxrd-uEiRknib16aFiOFXrCY8bFRw",
    'authDomain': "neurochat-4cd80.firebaseapp.com",
    'databaseURL': "https://neurochat-4cd80.firebaseio.com",
    'projectId': "neurochat-4cd80",
    'storageBucket': "neurochat-4cd80.appspot.com",
    'messagingSenderId': "612467327856",
    'appId': "1:612467327856:web:c0803434c65d4ade1d05b5",
    'measurementId': "G-3YDS4M32H5"
}
#   // Initialize Firebase
firebase=pyrebase.initialize_app(config)

auths=firebase.auth()
database=firebase.database()

def intro(requests):
    return render(requests, "pag1.html")

def signIn(requests):
    return render(requests, "mainPage.html")

  #this would happen after sign in
def postsign(requests):
    email=requests.POST.get('email')
    passw=requests.POST.get('pass')
    try:
      user=auths.sign_in_with_email_and_password(email,passw) #checking user
      session_id=user['idToken']  #requesting session
      requests.session['uid']=str(session_id)
    except:
        message="invalid credentials"
        return render(requests,"mainPage.html",{"messg":message})
    print(user['idToken'])
    return render(requests,'page3.html',{"e":email})

def quiz(requests):
    return render(requests,'quiz.html')    






def logout(requests):
    auth.logout(requests)
    msg="sucessfully logged out"
    return render(requests,"mainPage.html",{"messg":msg})    

def signUp(requests):
    return render(requests,"signUpform.html")   #signup form



def postsignUp(requests):
 email=requests.POST.get('email')
 passw=requests.POST.get('pass')
 name=requests.POST.get('Fname')
 friend1no=requests.POST.get('friend1no')
 friend2no=requests.POST.get('friend2no')

 user=auths.create_user_with_email_and_password(email,passw)
 uid=user['localId']

 data= {"name":name, "status":"1", "friend1no":friend1no,"friend2no":friend2no}
#storing data from registration form to variable data in dictionary
 database.child(uid).child("details").set(data)
 msg="Account created sucessfully, please login now"
 return render(requests,"mainPage.html",{"messg":msg})



def sendsms(requests):
     url='https://www.fast2sms.com/dev/bulk'

     idtoken=requests.session['uid'] 
     a=auths.get_account_info(idtoken)
     a =a['users']                             
     print(a)
     a =a[0]
     a =a['localId']
     print(a)

     name=database.child(a).child('details').child('name').get().val()                  #retriving data from firebase database
     firstFriendNumber=database.child(a).child('details').child('friend1no').get().val()       
     secondFriendNumber=database.child(a).child('details').child('friend2no').get().val()

     print(firstFriendNumber)
     print(name)
     para={
         'authorization':'XYmpiL3FWBhEcz50HxVuQDteI1RlUgojsSqCO2rGdwyMTvb9PkfaP6NUeFHvVAzjwTnXydOrkEKmo1Gt',
         'sender_id':"FSTSMS",
         'message':"your friend needs your help, plz contact him",
         'language':'english',
         "route":"p",
         'numbers':fristFriendNumber
         
     }   
    

     response=msgRequest.get(url, params=para)
     print(response.json())
     msg="message sent successfully"
     return render(requests,"page3.html",{"messg":msg})



