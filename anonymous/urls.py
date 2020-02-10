from django.urls import path
from . import views

urlpatterns = [
    path('',views.confessions, name='confessions'),
    path('anonymous/',views.anonymous, name='anonymous'),
    
]