from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile, name='profile'),
    path('changeprofilepic/',views.profilepic, name='profilepic'),
    path('edit/',views.editprofile, name='editprofile'),

]