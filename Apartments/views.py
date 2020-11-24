from django.shortcuts import render
from django.http import HttpResponse
from .models import Apartment
from django.conf import settings
from django.contrib import admin
from .forms import UserForm
from django.urls import reverse

import stripe

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

def index(request):
    stripe.api_key=settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HqqFGEHDBTTzNBJNQssOgod',
            'quantity': 1
                    }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('index')),
    )
    context={
            'session_id': session.id,
            'stripe_public_key': settings.STR
    }
    return render(request,'index.html')

#Dynamic Lookup views
#def dynami_lookup_views(request):
 #   obj=Apartment.objects.get(id=1)
  #  context=