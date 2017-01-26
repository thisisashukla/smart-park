from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

from Application import connector
from .forms import User_Form
from .forms import Parking_Form
from .models import User

# Create your views here.

def Registration_Main(request):
    
    if request.method=='GET':
        return render(request,'regis_main.html')
    
def User_Regis(request):
    
    if request.method=='GET':
        form=User_Form()
        
        return render(request,'user_regis.html',{'form':form})
    
    if request.method=='POST':
        print('in post')
        user_form=User_Form(request.POST)
        print(user_form)
        print(user_form.errors)
        if user_form.is_valid():
            print('form data valid')
            user_instance = user_form.save(commit=False)
            
            user_instance.name=user_form.cleaned_data['full_name']
            print(user_instance.name)
            user_instance.email=user_form.cleaned_data['email']
            print(user_instance.email)
            user_instance.password=user_form.cleaned_data['password']
            print(user_instance.password)
            user_instance.city=user_form.cleaned_data['city']
            print(user_instance.city)
            user_instance.save()
            print('saving data')
            context={'from':'User'}
            return render_to_response('Success.html',context)
        else:
            print('data invalid')
            context={'from':'User'}
            return render_to_response('Failure.html',context)




def Parking_Regis(request):
    
    if request.method=='GET':
        form=Parking_Form()
        
        return render(request,'parking_regis.html',{'form':form})
    
    if request.method=='POST':
        print('in post')
        parking_form=Parking_Form(request.POST)
        print(parking_form)
        print(parking_form.errors)
        if parking_form.is_valid():
            print('form data valid')
            parking_instance = parking_form.save(commit=False)
            
            parking_instance.owner_name=parking_form.cleaned_data['owner_name']
            print(parking_instance.owner_name)
            parking_instance.parking_name=parking_form.cleaned_data['parking_name']
            print(parking_instance.parking_name)
            parking_instance.capacity=parking_form.cleaned_data['capacity']
            print(parking_instance.capacity)
            parking_instance.lat=parking_form.cleaned_data['lat']
            print(parking_instance.lat)
            parking_instance.long=parking_form.cleaned_data['long']
            print(parking_instance.long)
            print('saving data')
            parking_instance.save()
            context={'from':'Parking'}
            return render_to_response('Success.html',context)
        else:
            print('data invalid')
            context={'from':'Parking'}
            return render_to_response('Failure.html',context)
    
            
            