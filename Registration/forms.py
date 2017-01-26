'''
Created on 09-Jan-2017

@author: MDSharma
'''
from django.forms import ModelForm
from django import forms
from Registration.models import User
from Registration.models import Parking

# class User_Form(forms.Form):
#     fullName=forms.CharField(label='fullName')
#     email=forms.EmailField(label='email')
#     password = forms.CharField(label='password',max_length=32, widget=forms.PasswordInput)
#     city=forms.ChoiceField(label='city',choices=['Mum','Lko'])

class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'city']
        
class Parking_Form(ModelForm):
    class Meta:
        model = Parking
        fields=['owner_name','parking_name','capacity','lat','long']
        widgets = {'lat': forms.HiddenInput(),'long':forms.HiddenInput()}        