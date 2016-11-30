from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def Location_Main(request):   
    return render(request,'Index.html')

def Location_pgr(request):
    return render(request,'pgr.html')

def Location_loc(request):
    return render(request,'location_index.html')
