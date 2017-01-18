'''
Created on 09-Jan-2017

@author: MDSharma
'''
from django.forms import ModelForm
from django import forms
from Registration.models import User
from Registration.models import Parking


class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'city']
        
class Parking_Form(ModelForm):
    class Meta:
        model = Parking
        fields=['owner_name','parking_name','capacity','lat','long']
        widgets = {'lat': forms.HiddenInput(),'long':forms.HiddenInput()}        