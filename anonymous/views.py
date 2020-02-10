from django.shortcuts import render,redirect
from django.conf import settings
from .models import AnonymousClass
from apps.models import Account
from apps.views import navbar
# Create your views here.
def anonymous(req):
    username='anonymous'
    if(req.user.is_authenticated ):
        username=req.user.username
    
    if(req.method=='POST'):
        anonymous=req.POST['anonymous']
        obj=AnonymousClass(username=username,anonymous=anonymous)
        obj.save()
        return redirect('/')
    else:
        return render(req,'anonymous.html',navbar(req))

def confessions(req):
    confessions = AnonymousClass.objects.all().order_by('-time').values_list('username','anonymous','time')
    print(confessions)
    admin = Account.objects.filter(is_admin=True).values_list('username',flat=True)
    ob1={'admin' : admin , 'confessions' : confessions }
    ob1.update(navbar(req))
    return render(req, 'home.html', ob1)