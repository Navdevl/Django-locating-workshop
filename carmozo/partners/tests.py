# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.test import TestCase
from .models import PartnersDetails,ContactDetails
# Create your tests here. 
class PartnersDetailsrTest(TestCase):

 def create_PartnersDetails(self, name="abcdefghijklmnopqrstuvwxyz", address="chamrajpet,Bengaluru",type="WORKSHOP",city="Bangalore",latitude=12.95701,longitude=77.563441):
  return PartnersDetails.objects.create(name=name, address=address,type=type,city=city,latitude=latitude,longitude=longitude)
#model
 def test_PartnersDetails_creation(self):
  w = self.create_PartnersDetails()
  self.assertTrue(isinstance(w, PartnersDetails))
  self.assertEqual(w.__unicode__(), w.name)
 
#views 
#SearchAddress
 def test_template(self):
  response = self.client.get("/search/")
  self.assertEqual(response.status_code, 200)
  self.assertTemplateUsed(response, "search.html")
#request_access
 def test_filter_list_view(self):
  w = self.create_PartnersDetails()
  
  resp = self.client.post('/filter/',json.dumps("chamrajpet,Bengaluru"),content_type='application/json',
                              HTTP_X_REQUESTED_WITH='XMLHttpRequest')
                

  self.assertEqual(resp.status_code, 200)
  self.assertJSONEqual(
            str(resp.content),
            dict = {
          "qwerty": [
          {
            "lat": "44.933493",
            "long": "7.540749",
          }
          ]
        }
      )
  
  
