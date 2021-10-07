from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class contactInfo(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


    def __str__(self):
        return self.name
