from django.shortcuts import render
import pyrebase
from django.contrib import auth
config={

    
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

  
def postsign(requests):
    email=requests.POST.get('email')
    passw=requests.POST.get('pass')
    try:
      user=auths.sign_in_with_email_and_password(email,passw)
      session_id=user['idToken']
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
    return render(requests,"signUpform.html")   



def postsignUp(requests):
    email=requests.POST.get('email')
    passw=requests.POST.get('pass')
    name=requests.POST.get('Fname')

    user=auths.create_user_with_email_and_password(email,passw)
    uid=user['localId']

    data= {"name":name, "status":"1"}

    database.child(uid).child("details").set(data)
    msg="Account created sucessfully, please login now"
    return render(requests,"mainPage.html",{"messg":msg})



