from django.db import models

# Create your models here.
class Apartment(models.Model):
    Unit=models.CharField(max_length=7)
    Price=models.FloatField(default=799.0)
    Description=models.TextField(blank=True,null=True)
    Occupied=models.BooleanField(default=False)
    Tenant_Name=models.TextField(default='Unoccupied')

    def __str__(self):
        return self.Unit
        return self.Price
        return self.Description
        return self.Occupied
        return self.Tenant_Name

class TenantUser(models.Model):
    First_Name=models.CharField(max_length=16,blank=False,null=True)
    Last_Name=models.CharField(max_length=16,blank=False,null=True)
    Unit=models.CharField(max_length=9,blank=False,null=True)
    

class Bills(models.Model):
    Category=models.CharField(max_length=16)
    Bill=models.IntegerField(default=0)
    TenantName=models.CharField(max_length=50)

class WorkOrders(models.Model):
    Issue=models.TextField()
    Resolved=models.BooleanField(default=False)

