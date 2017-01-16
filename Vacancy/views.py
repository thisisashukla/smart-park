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
                 
            
def vacancy_feed(request):
    print('vacancy_feed view')
    if request.method=='GET':
        pgcon= connector.postgresConnector('web_data')
        [conn,cur]=pgcon.getConnCur()    
        
        query='SELECT park.parking_name,ST_AsGeoJSON(ST_SetSRID(ST_MakePoint(park.long,park.lat),4326)),vac.vacancy from public."Registration_parking" as park, public."Vacancy_vacancy" as vac where vac.parking_id_id=park.parking_id'
        
        cur.execute(query)
        qresult=cur.fetchall()
        print(qresult)
        result=[]
        pointjson='{\"type\": \"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"properties\":{'
        append1='\"},\"geometry\":'
        append2='},{\"type\":\"Feature\",\"properties\":{'
        result.append(pointjson)
        print(result)
        for rows in range(0,len(qresult)-2):
            print('loop')
            result.append('\"name\":\"')
            result.append(str(qresult[rows][0]))
            #result.append('\",')
            print(result)
            result.append('\",\"vacancy\":\"')
            result.append(str(qresult[rows][2]))
            result.append(append1)
            result.append(str(qresult[rows][1]))
            result.append(append2)
    
        result.append('\"name\":\"')
        result.append(str(qresult[len(qresult)-1][0]))
        result.append('\",\"vacancy\":\"')
        result.append(str(qresult[len(qresult)-1][2]))
        result.append(append1)
        result.append(str(qresult[len(qresult)-1][1]))
        result.append('}]}')
        r = ''.join(str(v) for v in result)
        print(r)
        
        return HttpResponse(r)        
        