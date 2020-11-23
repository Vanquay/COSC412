from django import forms
from .models import TenantUser

class UserForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=TenantUser
        fields={'First_Name',
                'Last_Name',
                'SSN',
                'Username',
                'Password'
                }
    
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        if not email.contains('@'):
            raise forms.ValidationError('invalid email')
        return email
