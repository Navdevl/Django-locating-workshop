# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import admin
from .models import PartnersDetails,ContactDetails,PointOfInterest

# Register your models here.

class ContactInline(admin.TabularInline):
 model = ContactDetails

class PartnersAdmin(admin.ModelAdmin):
 inlines = (ContactInline, )
 list_display = ('name', 'type', 'code','status','address')
 search_fields = ['address',]
 list_filter=['status','type']


admin.site.register(PartnersDetails,PartnersAdmin)
admin.site.register(ContactDetails)
admin.site.register(PointOfInterest)