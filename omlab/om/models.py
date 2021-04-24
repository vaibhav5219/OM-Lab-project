from django.db import models

# Create your models here.

class OmLab(models.Model):
    img = models.ImageField(upload_to='media/images/%y/%m/%d')
    title = models.CharField (max_length= 200)
    passcode = models.CharField(max_length=10)

    def __str__(self):
        return self.title
