from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
#from .forms import BlogForm

def navbar(req):
    name='Krishnendu Chatterjee'
    phone_number='+917003033085'
    email='krishnenduchatterjee25@gmail.com'
    nav={ 'copyright' : { 'name' : name , 'phone_number' : phone_number , 'email' : email ,}
    }
    return nav

def base(req):
    return render(req , 'base.html' ,navbar(req))