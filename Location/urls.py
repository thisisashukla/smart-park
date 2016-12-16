'''
Created on 19 Nov 2016

@author: Ankur
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.Location_Main, name='Location_Main'),
    url(r'^pgr', views.Location_pgr, name='Location_pgr'),
    url(r'^loc',views.Location_loc,name='Location_loc'),
    url(r'^search',views.Location_search,name='Location_search'),
    url(r'(?P<num>[0-9]+)/(?P<co>\[.*\])',views.Location_route,name='Location_route'),
]

