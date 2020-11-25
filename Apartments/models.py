from django.db import models

# Create your models here.
class Apartment(models.Model):
    Unit=models.CharField(max_length=7)
    Price=models.FloatField(default=799.0)
    Description=models.TextField(blank=True,null=True)
    Occupied=models.BooleanField(default=False)
    Tenant_Name=models.TextField(default='Unoccupied')

class TenantUser(models.Model):
    First_Name=models.CharField(max_length=16,blank=False,null=True)
    Last_Name=models.CharField(max_length=16,blank=False,null=True)
    SSN=models.CharField(max_length=9,blank=False,null=True)
    Username=models.CharField(max_length=16,blank=False,null=True)
    Password=models.CharField(max_length=16,blank=False,null=True)

class Bills(models.Model):
    Category=models.CharField(max_length=16)
    Bill=models.IntegerField(default=0)

class WorkOrders(models.Model):
    Issue=models.TextField()
    Issue=models.BooleanField(default=False)

