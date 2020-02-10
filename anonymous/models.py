from django.db import models

# Create your models here.
class AnonymousClass(models.Model):
    username = models.CharField(max_length=100)
    anonymous = models.TextField()
    time = models.DateTimeField(verbose_name='text time', auto_now_add=True)

    def __str__(self):
        return (self.username)
