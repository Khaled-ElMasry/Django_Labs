"""day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from register.views import register, login,home,addstudent,update,deletestu,select,search

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('register',register),
    path('login', login),
    path('home',home),
    path('addstu', addstudent),
    path('update',update),
    path('delete',deletestu),
    path('select',select),
    path('search',search),
]
