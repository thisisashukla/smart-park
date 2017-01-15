from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from geojson import FeatureCollection
from psycopg2.extensions import AsIs
from SPark import connector
import urllib2
import json
import re

# Create your views here.

def Routing_Main(request):   
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
        
    #print(coordinate_array[2])
    #print(coordinate_array[3])
    
    #q="SELECT * FROM ways JOIN (SELECT * FROM pgr_dijkstra('SELECT class_id AS id, source, target, length AS cost FROM ways', 1, 1103, directed:=TRUE)) AS route ON ways.gid = route.edge"
    #cur.execute(q)
    #r=cur.fetchall()
    #print(r)
    #json_output = json.dumps(r)
    #print(json_output)
    
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
    
    
    #route_query='SELECT ST_AsGeoJSON(the_geom) AS geoj FROM ways JOIN (SELECT * FROM pgr_dijkstra(\'SELECT class_id AS id, source, target, cost_s AS cost FROM ways\', %s, %s, directed:=TRUE)) AS route ON ways.source = route.node;'
    #route_query='with temp as (SELECT the_geom,source,target,ways.cost FROM ways JOIN (SELECT * FROM pgr_dijkstra(\'SELECT class_id AS id, source, target, length AS cost FROM ways\', %s, %s, directed:=TRUE)) AS route ON ways.source = route.node) select ST_AsGeoJSON(the_geom) from temp where (temp.source,temp.cost) in (select temp.source,min(temp.cost) from temp group by temp.source);'
    #route_query='with temp as (SELECT ST_AsGeoJSON(the_geom), row_number() over (partition by source order by ways.cost)rownum FROM ways JOIN (SELECT * FROM pgr_dijkstra(\'SELECT class_id AS id, source, target, length AS cost FROM ways\', %s, %s, directed:=TRUE)) AS route ON ways.source = route.node) select * from temp where rownum=1;'    
    route_query='SELECT ST_AsGeoJSON(the_geom) AS geoj FROM ways JOIN (SELECT * FROM pgr_dijkstra(\'SELECT gid AS id, source, target, length AS cost FROM ways\', %s, %s, directed:=TRUE)) AS route ON ways.gid = route.edge'
    
    
    #cur.execute(route_query,(AsIs(source),AsIs(target)))
    cur.execute(route_query,(AsIs(source),AsIs(target)))
    result3=cur.fetchall()
    print('printing result')
    print(result3)
    #j=json.dumps(result3)
    
    
    #print('result3'+j)
    #FeatureCollection(result3)
    result=[]
    routejson='{\"type\": \"FeatureCollection\",\"crs\": {\"type\": \"name\",\"properties\":{\"name\": \"EPSG:4326\"}},\"features\":[{\"type\":\"Feature\",\"geometry\":'
    append='},{\"type\":\"Feature\",\"geometry\":'
    #temp=''
    result.append(routejson)
    for rows in range(0,len(result3)-2):
        #print(str(result3[rows]))
        #temp=str(re.findall('{(.*)}',str(result3[rows])))
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
    #ob='{\"type\": \"FeatureCollection\",\"crs\": {\"type\": \"name\",\"properties\":{\"name\": \"EPSG:4326\"}},\"features\":[{\"type\":\"Feature\",\"geometry\":{\"type\": \"MultiLineString\",\"coordinates\": [[[72, 19], [73, 19]],[[73, 19], [73, 18]],[[73, 18], [72, 18]],[[72, 18], [73, 18]]]}}]}'
    #print(json.dumps(r))
#     pgcon= connector.postgresConnector('map_data')
#     [conn,cur]=pgcon.getConnCur()
#     nearest_geom='SELECT ST_AsGeoJSON(the_geom) as geoj,source,target,name,gid FROM ways r  order by ST_Distance(r.the_geom,ST_SetSRID(ST_MakePoint(%s, %s),4326));'
#     #coordinate_array=re.findall('\d+\.\d+',co)
#     cur.execute(nearest_geom,('72.91799708106399','19.13197880008622'))
#     r=cur.fetchone()
#     print(r)
#     routejson='{\"type\": \"FeatureCollection\",\"crs\": {\"type\": \"name\",\"properties\":{\"name\": \"EPSG:4326\"}},\"features\":[{\"type\":\"Feature\",\"geometry\":'
#     #print(re.findall('\'(.*)\'',str(r[0])))
#     result=[]
#     result.append(routejson)
#     result.append(str(r[0]))
#     print(result)
#     result.append('}]}')
#     print(result)
#     r = ''.join(str(v) for v in result) 
#     print(r)
#     pgcon.closeConnection(conn, cur)
    
    #return HttpResponse(r)

    return HttpResponse(r)

