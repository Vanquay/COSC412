from django.db import models

# Create your models here.
class Apartment(models.Model):
    Unit=models.CharField(max_length=7)
    Price=models.FloatField(default=799.0)
    Description=models.TextField(blank=True,null=True)
    Occupied=models.BooleanField()
    Tenant_Name=models.TextField(default='Unoccupied')
