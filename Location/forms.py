from django import forms

class GeoSeach_Form(forms.Form):
    location=forms.CharField(label='location')
    