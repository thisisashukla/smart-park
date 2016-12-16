'''
Created on 8 Dec 2016

@author: Ankur
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.Regis_Main, name='Registration_Main'),
    url(r'^parking', views.Parking, name='Parking'),
    url(r'^user',views.User,name='User'),
    
]
