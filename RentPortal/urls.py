"""RentPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Apartments import views


urlpatterns = [

        path('home/',views.registration_view,name='register'),
        path('login/',views.login_view,name='login'),
        path('logout/',views.logout_view,name='logout'),

    path('',views.homepage_view,name='home'),
    path('complaint/',views.complaint_view,name='complaint'),
    path('admin/', admin.site.urls),
    path('workThanks/',views.workOrderThanks_view,name='workOrderThanks'),
    path('registerlogin/',views.registration_view),
    path('payment/',views.payment_view,name='payment'),
    path('product/',views.apartment_detail_view),
    path('checkout/',views.index,name='index'),
    path('thanks/',views.thanks,name='thanks')
]
