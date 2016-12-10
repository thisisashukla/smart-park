from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Parking(models.Model):
    name=models.CharField(max_length=50)
    lati=models.FloatField()
    longi=models.FloatField()

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    