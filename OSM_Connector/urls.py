'''
Created on 15-Jan-2017

@author: MDSharma
'''
from django.conf.urls import url
from . import views

urlpatterns=[
    #url(r'^$', views.Location_Main, name='Location_Main'),
    #url(r'(?P<num>[0-9]+)/(?P<co>\[.*\])',views.snap_coordinate,name='Location_route'),
    url(r'(?P<left>[0-9]+)/(?P<upper>[0-9]+)/(?P<right>[0-9]+)/(?P<bottom>[0-9]+)',views.bbox_downloader,name='BBOX_downloader')
]

