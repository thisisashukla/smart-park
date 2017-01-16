from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Parking(models.Model):
    parking_id = models.AutoField(primary_key=True)
    owner_name=models.CharField(max_length=50)
    parking_name=models.CharField(max_length=50)
    capacity=models.IntegerField()
    lat=models.FloatField()
    long=models.FloatField()
 #   class Meta:
  #      app_label='registration'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    CITY = (
        ('Mum', 'Mumbai'),
        ('Lko', 'Lucknow'),
    )
    city = models.CharField(max_length=3, choices=CITY)
  #  class Meta:
   #     app_label='registration'
    
