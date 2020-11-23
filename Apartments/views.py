from django.shortcuts import render
from django.http import HttpResponse
from .models import Apartment
from .forms import UserForm

# Create your views here.
def homepage_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return HttpResponse("<h1>Welcome to the Rent Portal</h1>") #String of HTML Code

def home_view(request,*args,**kwargs):
    return render(request,'home.html')

def complaint_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"complaint.html")

def payment_view(request,*args,**kwargs):
    context={'Ad':'We love having you in our facility',
            'Contact':6672283425}
    return render(request,'payment.html',context)

#Model Views
def apartment_detail_view(request):
    obj=Apartment.objects.get(id=1)
    context={'object':obj}
    return render(request,'Apartment/detail.html',context)

#Form Views
def userLogin_form_view(request):
    form=UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UserForm()

    context={'form': form}
    return render(request,'userLogin.html',context)