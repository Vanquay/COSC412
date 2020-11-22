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