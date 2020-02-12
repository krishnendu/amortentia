from django import forms
from .models import Ridikkulus

import pyrebase
import os


config = {
  "apiKey": "AIzaSyD0PCbMOplAFK7w6zREOPNjVaSd_FL_6yo",
  "authDomain": "first-hosting-ff171.firebaseapp.com",
  "databaseURL": "https://first-hosting-ff171.firebaseio.com",
  "storageBucket": "first-hosting-ff171.appspot.com"
}

firebase = pyrebase.initialize_app(config)

class RidikkulusForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter first name'}), label='First Name', max_length=50 )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter last name'}), label='Last Name', max_length=50 )
    university_roll = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder' : 'Enter University Roll'}), label='University Roll', max_length=11, min_length=11 )
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'  , 'placeholder' : 'Enter Caption'} ),label='Caption' )
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control' ,'accept': 'image/*'}),label='Choose a picture')

    class Meta:
        model = Ridikkulus
        fields =('first_name','last_name','university_roll','img','caption')
    
    def save(self):
        photo = super(RidikkulusForm, self).save()
        storage = firebase.storage()
        # as admin
        storage.child(str(photo.img)).put(str(photo.img.path))
        print(storage.child(str(photo.img)).get_url(None))
        photo.image=storage.child(str(photo.img)).get_url(None)
        os.remove(str(photo.img.path))
        photo.img = None
        photo.save()