from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from psycopg2.extensions import AsIs
from django.views.decorators.csrf import csrf_exempt
import re


from .models import Vac2
from Registration.models import Parking
from Vacancy.forms import Vacancy_Form
from Application import connector

# Create your views here.
@csrf_exempt
def server_register(request):
    #vacancy_form=Vacancy_Form(request.POST)
    #print(vacancy_form)
    #print(vacancy_form.is_valid())
    #print(vacancy_form.errors)
    postData=request.POST
    gsm_id=postData['gsm_id']
    parking_id=postData['parking_id']
    vaca=int(postData['vacancy'])
    print(gsm_id)
    print(parking_id)
    print(vaca)

    if request.method=='POST':
        print("in vacancy post")
        #print(parking_form)
        parking_instance=Parking.objects.filter(parking_id=parking_id)
        print(parking_instance)

        #add lat long verification code
        if parking_instance:
            print('valid parking instance found')
            vacancy_instance=Vac2.objects.filter(gsm_id=gsm_id)
            if(vacancy_instance):
                print('valid gsm_id presented')
                context={'msg':'success'}
                return HttpResponse(request,context)
            else:
                cap=parking_instance[0].capacity
                vac=Vac2(gsm_id=gsm_id,parking_id=parking_id,vacancy=cap)
                vac.save()
                print("gsm registered successfully")
            # if lat==parking_instance.lat and long==parking_instance.long:
            #     print('valid geolocation')
            #     context={'msg':'registration_successful','parking_id':parking_instance.parking_id}
            #     return HttpResponse(request,context)
            # else:
            #     print('invalid geolocation')
            #     context={'msg':'registration_failed'}
            #     return HttpResponse(request,context)
                context={'msg':'success'}
                return HttpResponse(request,context)
        else:
            print('invalid id')
            context={'msg':'invalid id'}
            return HttpResponse(request,context)
    else:
        context={'msg':'invalid request'}
        return HttpResponse(request,)


@csrf_exempt
def parking_vacancy(request,gsm_id=0,parkingId=0,vacancy=0):

    if request.method=='POST':
        pgcon= connector.postgresConnector('web_data')
        [conn,cur]=pgcon.getConnCur()

        #id_query='select * from Registration_parking where parking_id=%s'
        #cur.execute(id_query,(AsIs(parking_id)))

        parking_instance=int(Parking.objects.filter(parking_id=parkingId))
        print(parking_instance)
        #add lat long verification code
        if parking_instance:
            print('valid parking instance')
            vac=Vac2.objects.filter(parking_id=parkingId)
            if(vac):
                print('valid vacancy instance')
                vac.vacancy=vac.vacancy-1
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

        query='SELECT park.parking_name,ST_AsGeoJSON(ST_SetSRID(ST_MakePoint(park.long,park.lat),4326)),vac.vacancy from public."Registration_parking" as park, public."Vacancy_vac2" as vac where vac.parking_id=park.parking_id'

        cur.execute(query)
        qresult=cur.fetchall()
        print(qresult)
        result=[]
        pointjson='{\"type\": \"FeatureCollection\",\"features\":[{\"type\":\"Feature\",\"properties\":{'
        append1='\"},\"geometry\":'
        append2='},{\"type\":\"Feature\",\"properties\":{'
        result.append(pointjson)
        print(result)
        for rows in range(0,len(qresult)-1):
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
        pgcon.closeConnection(conn, cur)
        return HttpResponse(r)
