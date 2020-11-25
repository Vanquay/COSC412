from django import forms
from django.forms import ModelForm
from .models import TenantUser,WorkOrders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1','password2']

class WorkOrderForm(ModelForm):
    class Meta:
        model=WorkOrders
        fields={'Issue'}
