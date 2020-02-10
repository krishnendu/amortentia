from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.conf import settings
from apps.models import Account,ProfilePicture,user
from apps.views import navbar
from .forms import ProfilePictureForm,UserForm

# Create your views here.

def profile(req):
    username=req.user.username
    if not req.user.is_authenticated :
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    if req.user.is_authenticated :
        ob1={'user' : Account.objects.get(username=username) }
        ob1.update(navbar(req))
        ob3={ 'username' : req.user.username }
        ob4={ 'pp' : ProfilePicture.objects.get(id=Account.objects.get(username=username).id).img }
        ob5={ 'user1' : user.objects.get(id=Account.objects.get(username=username).id) }
        ob1.update(ob3)
        ob1.update(ob4)
        ob1.update(ob5)
        return render(req,'userinfo.html',ob1)
    else:
        #pp=ProfilePicture(id=req.user.id)
        #pp.save()
        #user1=user.account(Account.objects.get(id=req.user.id))
        #user1.save()
        return redirect('/profile/')

def profilepic(req):
    if not req.user.is_authenticated :
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    id=Account.objects.get(username=req.user.username).id
    instance =get_object_or_404(ProfilePicture, id=id)
    form=ProfilePictureForm(req.POST or None, req.FILES or None ,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/profile')
    ob1={'form' : form}
    ob1.update(navbar(req))
    return render(req,'changeprofilepic.html',ob1)


def editprofile(req):
    if( not req.user.is_authenticated ):
        return redirect('%s?next=%s' % (settings.LOGIN_URL, req.path))
    id=user.objects.get(id=Account.objects.get(username=req.user.username).id).id
    instance =get_object_or_404(user, id=id)
    form=UserForm(req.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/profile')
    ob1={'form' : form}
    ob1.update(navbar(req))
    return render(req,'edit.html',ob1)

