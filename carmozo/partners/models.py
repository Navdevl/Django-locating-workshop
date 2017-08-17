# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
import requests
# Create your models here.
categories = (
    ('select', 'SELECT'),
    ('W', 'WORKSHOP'),
    ('M', 'MECHANIC'),
)
cities = (
    ('select', 'SELECT'),
    ('B', 'Banglore'),
    ('H', 'Hyderabad'),
)
options = (
    ('select', 'SELECT'),
    ('A', 'Active'),
    ('I', 'Inactive'),
)
class PartnersDetails(models.Model):
 
 name = models.CharField(max_length=20)
 address = models.CharField(max_length=80)
 type = models.CharField(max_length=20,choices=categories,default='select')
 city = models.CharField(max_length=20,choices=cities,default='select')
 code = models.CharField(primary_key=True,max_length=20)
 latitude = models.DecimalField(
               max_digits=9, decimal_places=6, null=True, blank=True)
 longitude = models.DecimalField(
               max_digits=9, decimal_places=6, null=True, blank=True)
 status = models.CharField(max_length=20,choices=options,default='select')			   
 def __str__(self):
    return self.name 
 def __unicode__(self):
    return self.name	
 def save(self, *args, **kwargs):
      address = self.address
      api_key = "AIzaSyAo8tCXTMOAD-Y2cLXzcI-AJur9kx2Fw8o"
      api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
      api_response_dict = api_response.json()

      
      latitude = api_response_dict['results'][0]['geometry']['location']['lat']
      longitude = api_response_dict['results'][0]['geometry']['location']['lng']
      self.latitude = latitude
      self.longitude = longitude
      super(PartnersDetails, self).save(*args, **kwargs) # Call the "real" save() method.
 #address = "Telecom Layout, Jakkuru, Bengaluru, Karnataka 560064, India"
 #api_key = "AIzaSyAo8tCXTMOAD-Y2cLXzcI-AJur9kx2Fw8o"
 #api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
 #api_response_dict = api_response.json()

 
 #latitude = api_response_dict['results'][0]['geometry']['location']['lat']
 #longitude = api_response_dict['results'][0]['geometry']['location']['lng']
 #print 'Latitude:', latitude
 #print 'Longitude:', longitude
	

 	
	
class ContactDetails(models.Model):
 wname = models.OneToOneField(PartnersDetails, on_delete=models.CASCADE)
 contact_number1=models.CharField(max_length=15,blank=False)
 contact_number2=models.CharField(max_length=15)
 
 def __str__(self):
    return "%s"% self.id
	
	
class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
	
    def __str__(self):
     return "%s"% self.name
		
 