from django.shortcuts import render,redirect
from django.conf import settings
from .models import AnonymousClass
from django.contrib import messages
from apps.views import navbar
# Create your views here.
def anonymous(req):
    if(req.method=='POST'):
        anonymous=req.POST['anonymous']
        obj=AnonymousClass(anonymous=anonymous)
        obj.save()
        messages.success(req,"Confession saved")
        return redirect('/confession')
    else:
        return render(req,'confession.html',navbar(req))

