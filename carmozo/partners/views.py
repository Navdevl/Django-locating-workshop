# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import PartnersDetails,ContactDetails,PointOfInterest
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render_to_response
import json
import requests
from math import sin, cos, sqrt, atan2, radians
# Create your views here.
def SearchAddress(request):
 obj = PartnersDetails.objects.all()
 return render(request, "search.html", {'content':obj})

def insertIntoDataStruct(name,addlat,addlong,aDict):
    if not name in aDict:
        aDict[name] = [{'lat':addlat,'long':addlong}]
    else:
        aDict[name].append((addlat,addlong))
def request_access(request):
 print("DJANGO VIEW")
 if request.method == "POST":
  address = request.POST.get('request_data')  #User input
  api_key = "AIzaSyAo8tCXTMOAD-Y2cLXzcI-AJur9kx2Fw8o"  #GoogleAPIKey
  api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
  api_response_dict = api_response.json()
  #latitude and longitude of user input
  latitude = api_response_dict['results'][0]['geometry']['location']['lat']
  longitude = api_response_dict['results'][0]['geometry']['location']['lng']
  # approximate radius of earth in km
  R = 6371.0
  lat1 = radians(latitude)
  lon1 = radians(longitude)
  objs = PartnersDetails.objects.all()
  temp = {}
  for obj in objs:
   if obj.status == 'A':
    lat2 = radians(obj.latitude)
    lon2 = radians(obj.longitude)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #distance calculated between two points
    distance = R * c
    #Filtering places
    if distance < 5:    #setting radius of 5km
     insertIntoDataStruct(obj.code,obj.latitude,obj.longitude,temp)
  print "%f %f"% (latitude,longitude)
  print temp
  return JsonResponse(temp)
 return HttpResponse("Error Found")
 
