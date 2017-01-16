from __future__ import unicode_literals

from django.db import models
from Registration.models import Parking
# Create your models here.
class Vacancy(models.Model):
    gsm_id = models.CharField(max_length=50,primary_key=True)
    parking_id = models.ForeignKey(Parking,on_delete=models.CASCADE)
    vacancy = models.IntegerField()
