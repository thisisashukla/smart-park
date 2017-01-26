from django.forms import ModelForm
from django import forms
from Vacancy.models import Vacancy

# class User_Form(forms.Form):
#     fullName=forms.CharField(label='fullName')
#     email=forms.EmailField(label='email')
#     password = forms.CharField(label='password',max_length=32, widget=forms.PasswordInput)
#     city=forms.ChoiceField(label='city',choices=['Mum','Lko'])

class Vacancy_Form(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['gsm_id', 'parking_id', 'vacancy']
