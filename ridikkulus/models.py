from django.db import models
from datetime import datetime

# Create your models here.
class Ridikkulus(models.Model):
    first_name = models.CharField(max_length=50 )
    last_name = models.CharField(max_length=50 )
    university_roll = models.IntegerField()
    image = models.URLField(null=True)
    img = models.ImageField(upload_to='images/',null=True)
    caption = models.CharField(max_length=500 , blank=True , null=True)
    time = models.DateTimeField(verbose_name='upload time', auto_now_add=True)

    def __str__(self):
        return (self.first_name+' '+self.last_name)