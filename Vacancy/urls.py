'''
Created on 10-Jan-2017

@author: MDSharma
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    #url(r'^$', views.Registration_Main, name='Registration_Main'),
    url(r'Server_regis',views.server_register,name='Server_Register'),
    url(r'(?P<gsm_id>.*)/(?P<parking_id>.*)/(?P<vacancy>[0-9]+)',views.parking_vacancy,name='Parking_vacancy'),
    url(r'Feed_Layer',views.vacancy_feed,name='vacancy_feed'),
    ]
