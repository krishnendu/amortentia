from django.db import models

# Create your models here.
class AnonymousClass(models.Model):
    anonymous = models.TextField()
    time = models.DateTimeField(verbose_name='text time', auto_now_add=True)

    def __str__(self):
        return (str(self.time))
