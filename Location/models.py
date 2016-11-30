from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Parking(models.Model):
    name=models.CharField(max_length=50)
    lati=models.FloatField()
    longi=models.FloatField()

class Vacancy(models.Model):
    p_id=models.ForeignKey(Parking,on_delete=models.CASCADE)
    capacity=models.IntegerField()
    vacancy=models.IntegerField()
    up_time=models.DateTimeField()    
