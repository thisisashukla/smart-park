from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import urllib2
import json
import re
from geojson import FeatureCollection
from psycopg2.extensions import AsIs
from Application import connector

# Create your views here.

def Location_Main(request):   
    if(request.method=='GET'):
        return render(request,'Index.html')
            
def snap_coordinate(request,num="1",co=['']):
    #num=request.GET.get('num')
    print('hi i am in route view')
    print (num) 
    print(co)
    
    #getconnection
    pgcon= connector.postgresConnector('map_data')
    [conn,cur]=pgcon.getConnCur()
    
    coordinate_array=re.findall('\d+\.\d+',co)
    for coo in coordinate_array:
        print(coo)
        
    
    #finding closest road to source point
    closest_query='select w.source, w.target, ST_Distance(w.the_geom,ST_SetSRID(ST_MakePoint(%s, %s),4326)) as d from ways as w WHERE ST_DWithin(ST_SetSRID(ST_MakePoint(%s, %s),4326), w.the_geom, 100) order by d'
    print(coordinate_array[2])
    print(coordinate_array[3])
    cur.execute(closest_query,(coordinate_array[2],coordinate_array[3],coordinate_array[2],coordinate_array[3]))
    result1=cur.fetchone()
    
    closest_query='select w.source, w.target, w.name, ST_Distance(w.the_geom,ST_SetSRID(ST_MakePoint(%s, %s),4326)) as d from ways as w WHERE ST_DWithin(ST_SetSRID(ST_MakePoint(%s, %s),4326), w.the_geom, 100) order by d'
    print(coordinate_array[4])
    print(coordinate_array[5])
    cur.execute(closest_query,(coordinate_array[4],coordinate_array[5],coordinate_array[4],coordinate_array[5]))
    result2=cur.fetchone()
    
    print(result1)
    print(result2)
    s=result1[0]
    t=result2[1]  
    print(s)
    print(t)    
    pgcon.closeConnection(conn, cur)
    
    
    
    return HttpResponse(str(s)+' '+str(t))

def route(request,source=0,target=0):
    print(source)
    print(target)
    
    print('executing routing query')
    pgcon= connector.postgresConnector('map_data')
    [conn,cur]=pgcon.getConnCur()
    
    
    route_query='SELECT ST_AsGeoJSON(the_geom) AS geoj FROM ways JOIN (SELECT * FROM pgr_dijkstra(\'SELECT gid AS id, source, target, length AS cost FROM ways\', %s, %s, directed:=TRUE)) AS route ON ways.gid = route.edge'
    
    
    #cur.execute(route_query,(AsIs(source),AsIs(target)))
    cur.execute(route_query,(AsIs(source),AsIs(target)))
    result3=cur.fetchall()
    print('printing result')
    print(result3)
    result=[]
    routejson='{\"type\": \"FeatureCollection\",\"crs\": {\"type\": \"name\",\"properties\":{\"name\": \"EPSG:4326\"}},\"features\":[{\"type\":\"Feature\",\"geometry\":'
    append='},{\"type\":\"Feature\",\"geometry\":'
    #temp=''
    result.append(routejson)
    for rows in range(0,len(result3)-2):
        print(re.findall('\'(.*)\'',str(result3[rows]))[0])
        result.append(re.findall('\'(.*)\'',str(result3[rows]))[0])
        result.append(append)
    
    result.append(re.findall('\'(.*)\'',str(result3[len(result3)-1]))[0])
    result.append('}]}')
    print(result)
    r = ''.join(str(v) for v in result)            
    #r=''.join(result)
    print r 
    pgcon.closeConnection(conn, cur)
    #print(result)
    print(r)
    
    return HttpResponse(r)

