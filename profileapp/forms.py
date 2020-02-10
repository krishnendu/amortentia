from django import forms
from PIL import Image
from apps.models import ProfilePicture , user 


class ProfilePictureForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = ProfilePicture
        fields = ('img', 'x', 'y', 'width', 'height', )
        widgets = {
            'img': forms.FileInput(attrs={
                'accept': 'image/*'  # this is not an actual validation! don't rely on that!
            })
        }

    def save(self):
        photo = super(ProfilePictureForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.img)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.img.path)

        return photo


class UserForm(forms.ModelForm):
    universityroll = forms.CharField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder' : 'Enter University Roll'}), label='University Roll', max_length=11, min_length=11 )
    dob = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}),label='Date of Birth')
    sex=forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Enter Sex'}), label='Sex', max_length=10 )
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'  , 'placeholder' : 'Enter Bio'} ),label='Bio' , required=False )
        
    class Meta:
        model = user
        fields = ('universityroll','dob','sex','bio')

