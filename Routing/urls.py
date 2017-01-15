'''
Created on 19 Nov 2016

@author: Ankur
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^',views.Routing_Main,name='Routing_loc'),
    url(r'(?P<num>[0-9]+)/(?P<co>\[.*\])',views.snap_coordinate,name='Routing_route'),
    url(r'(?P<source>[0-9]+)/(?P<target>[0-9]+)',views.route,name='Routing_route')
]

