from django.db import models

# Create your models here.
class Apartment(models.Model):
    Unit=models.CharField(max_length=7)
    Price=models.FloatField(default=799.0)
    Description=models.TextField(blank=True,null=True)
    Occupied=models.BooleanField(default=False)
    Tenant_Name=models.TextField(default='Unoccupied')

class TenantUser(models.Model):
    First_Name=models.TextField()
    Last_Name=models.TextField()
    SSN=models.CharField(max_length=9)
    Username=models.TextField()
    Password=models.CharField(max_length=9)

class Bills(models.Model):
    Category=models.CharField(max_length=16)
    Bill=models.IntegerField()
    

    

