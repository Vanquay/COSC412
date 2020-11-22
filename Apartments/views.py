from django.shortcuts import render
from django.http import HttpResponse

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

def UserLogin_view(request,*args,**kwargs):
    return render(request,'UserLogin.html')

def payment_view(request,*args,**kwargs):
    context={'Ad':'We love having you in our facility',
            'Contact':6672283425}
    return render(request,'payment.html',context)

#Model Views
def apartment_view(request):
    obj=Apartment.objects.get(id=1)
    context={'Unit':obj.Unit,
            'Tenant': obj.Tenant_Name}
    return render(request,'product/detail.html',context)
