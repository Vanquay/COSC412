from django.contrib import admin

from .models import Apartment,Bills,TenantUser
# Register your models here.
admin.site.register(Apartment)
admin.site.register(TenantUser)