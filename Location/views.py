from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import urllib2
import json



from .forms import GeoSeach_Form
# Create your views here.

def Location_Main(request):   
    return render(request,'Index.html')

def Location_pgr(request):
    return render(request,'pgr.html')

def Location_loc(request):
    return render(request,'location_index.html')


def Location_search(request):
    
    if request.method=='GET':
        form=GeoSeach_Form()
        
        return render(request,'geo_search.html',{'form':form})
    
    if request.method=='POST':
        
        gform=GeoSeach_Form(request.POST)
        
        if gform.is_valid():
            data=gform.cleaned_data['location']
            print(data)
            
            searchstring='+'.join(data.split(' '))
            
            print(searchstring)
            
            path='http://www.mapquestapi.com/geocoding/v1/address?key='+'eGaI1nxMkc1QNqsdR1aqlMpa2yLdJbai&inFormat=kvp&outFormat=json'+'&location='+searchstring
            print (path)
            #jdata = json.load(urllib2.urlopen(path))
            
           # print (jdata)
            
            print("now using google api")
            
            path='https://maps.googleapis.com/maps/api/geocode/json?address='+searchstring+'&key=AIzaSyDhMx80fhKJpvteI_6as-4LMmPnQ4fPkBs'
            
            
            #jdata = json.load(urllib2.urlopen(path))
            
            #trying osm
            path='http://nominatim.openstreetmap.org/search?q='+searchstring+'&format=json&polygon=1&addressdetails=1'
            jdata = json.load(urllib2.urlopen(path))
            
            
            
            print (jdata)
            
            
        return render(request,'geo_search.html')
        
            
        
        
        
    
        
    
    

