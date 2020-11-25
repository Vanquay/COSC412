from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.contrib import admin,messages
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.urls import reverse

import stripe

# Create your views here.
def homepage_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return HttpResponse("<h1>Welcome to the Rent Portal</h1>") #String of HTML Code

def home_view(request,*args,**kwargs):
    return render(request,'home.html')

def registration_view(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account made for ' + user)
            return redirect('login')

    context={'form': form}
    return render(request,'register.html',context)

def login_view(request,*args,**kwargs):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('payment')
        else:
            messages.info(request,'Username or Password is incorrect')
        
    context={}
    return render(request,'login.html',context)

def logout_view(requets,*args,**kwargs):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def complaint_view(request,*args,**kwargs):
    print('Welcome ' + request.user)
    if request.method='POST':
        form=WorkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    
    return render(request,"complaint.html",context)

@login_required(login_url='login')
def payment_view(request,*args,**kwargs):
    context={'Ad':'We love having you in our Apartments',
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

@login_required(login_url='login')
def thanks(request):
    return render(request, 'thanks.html')

@login_required(login_url='login')
def index(request):
    stripe.api_key=settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1HqqFGEHDBTTzNBJNQssOgod',
            'quantity':1
                    }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('index')),
    )
    context={
            'session_id': session.id,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request,'index.html',context)

#Dynamic Lookup views
#def dynami_lookup_views(request):
 #   obj=Apartment.objects.get(id=1)
  #  context=