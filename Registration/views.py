from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Reg_User
# Create your views here.


def Regis_Main(request):   
    return render(request,'Reg_Main.html')

def Parking(request):
    return render(request,'Reg_Parking.html')

def User(request):
    
    if request.method=='GET':
        form=Reg_User()
        return render(request,'Reg_User.html',{'form':form})
    
    if request.method=='POST':
        form=Reg_User(request.POST)
        
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']   
            return render(request,'User_Success.html',{'name':name,'email':email})
     
        
