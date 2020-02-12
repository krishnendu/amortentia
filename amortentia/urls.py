"""amortentia URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from ridikkulus.views import ridikkulus as ridikkulus_view ,home as redirect_view,redirectview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anonymous.urls')),
    path('ridikkulus/' , ridikkulus_view ,name='ridikkulus' ),
    path('<str:url>/', redirectview , name='redirect'),
    path('', redirect_view , name='redirect'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
