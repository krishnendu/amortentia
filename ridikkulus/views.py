from django.shortcuts import render
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from .models import Ridikkulus
from .forms import RidikkulusForm
from apps.views import navbar
# Create your views here.

def ridikkulus(req):
    
    if(req.method=='POST'):
        form = RidikkulusForm(req.POST,req.FILES)
        if(form.is_valid()):
            form.save()
            messages.success(req,"Submitted Successfully")
        else:
            messages.error(req, 'Submission failed , Enter properly')
        return redirect('/ridikkulus')
    else :
        ob1={'form' : RidikkulusForm()}
        ob1.update(navbar(req))
        return render(req , 'ridikkulus.html',ob1)

def home(req):
    return redirect('/ridikkulus')

def redirectview(req,url):
    return redirect('/ridikkulus')