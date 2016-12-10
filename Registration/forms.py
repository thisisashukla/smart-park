'''
Created on 8 Dec 2016

@author: Ankur
'''
from django import forms

class Reg_User(forms.Form):
    name=forms.CharField(label='name')
    email=forms.EmailField()
    
    
    