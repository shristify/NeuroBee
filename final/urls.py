

"""cpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.intro, name='intro'),
    path('login.html/',views.signIn, name='signin'),
    path('postsign/', views.postsign, name='postsign'),
    path('logout/', views.logout, name='log'),
    path('signup.html/', views.signUp, name='signup'),
    path('postsignUp', views.postsignUp, name='postsignup'),
    path('signup.html/postsignUp/', views.postsignUp, name='postsignup'),
    path('sendsms/', views.sendsms, name='sendsms'),
    path('doctorsnearme/', views.DocsNear, name='maps'),
    path('quiz/', views.quiz, name='quiz'),
    path('you/', views.you, name='you'),
   





]
