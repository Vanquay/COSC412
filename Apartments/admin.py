from django.contrib import admin
from django.contrib.admin import AdminSite
from django.http import request
from django.http import HttpResponse
from django.shortcuts import render

from .models import Apartment,TenantUser,WorkOrders,Bills

# Register your models here.
admin.site.site_header='StingyMeany Rent Portal'
admin.site.site_title='StingyMeany Rent Portal'
admin.site.index_title='Admin ' + 'Logged in'
admin.site.register(Apartment)
admin.site.register(TenantUser)
admin.site.register(WorkOrders)
admin.site.register(Bills)