from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('savedata',views.savedata,name="savedata"),
    path('sellerpage',views.sellerpage,name="sellerpage"),
    path('registration',views.registration,name="registration"),
    # path('userlogin',views.userlogin,name="userlogin"),
    path('savecontact',views.savecontact,name="savecontact"),
    path('search',views.search,name="search"),

    path('displayplantsforsale',views.displayplantsforsale,name="displayplantsforsale"),


]