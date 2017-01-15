from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from psycopg2.extensions import AsIs

from SPark import connector
from .models import Vacancy
from Registration.models import Parking


# Create your views here.
def server_register(request,gsm_id=" ",lat=0.0,long=0.0):
    
    if request.method=='POST':
        parking_instance=Parking.objects.filter(gsm_id=gsm_id)
        print(parking_instance)
        #add lat long verification code
        if parking_instance:
            print('valid gsm_id presented')
            if lat==parking_instance.lat and long==parking_instance.long:
                print('valid geolocation')
                context={'msg':'registration_successful','parking_id':parking_instance.parking_id}
                return HttpResponse(request,context)
            else:
                print('invalid geolocation')
                context={'msg':'registration_failed'}
                return HttpResponse(request,context)
        else:
            print('invalid id')
            context={'msg':'invalid id'}
            return HttpResponse(request,context)
                
                
    
def parking_vacancy(request,gsm_id=" ",parkingId=" ",vacancy=0,lat=0.0,long=0.0):
    
    if request.method=='POST':
        pgcon= connector.postgresConnector('web_data')
        [conn,cur]=pgcon.getConnCur()
        
        #id_query='select * from Registration_parking where parking_id=%s'
        #cur.execute(id_query,(AsIs(parking_id)))
        
        parking_instance=Parking.objects.filter(parking_id=parkingId)
        print(parking_instance)
        #add lat long verification code
        if parking_instance:
            vac=Vacancy.objects.get(pk=1)
            park_id=Parking.objects.get(parking_id=parkingId)
            vac.parking_id=park_id
            vac.vacancy=vacancy
            
            vac.save()
            context={'msg':'success'}
            return HttpResponse(request,context)
        else:
            context={'msg':'wrong id'}
            return HttpResponse(request,context)
                 
            
        
        