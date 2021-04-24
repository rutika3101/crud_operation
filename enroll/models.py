from django.db import models


# Create your models here.

class register(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
