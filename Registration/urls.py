'''
Created on 09-Jan-2017

@author: MDSharma
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.Registration_Main, name='Registration_Main'),
    url(r'^User', views.User_Regis, name='User_Regis'),
    url(r'^Parking', views.Parking_Regis, name='Parking_Regis')
    ]