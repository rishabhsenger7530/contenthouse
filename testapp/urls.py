from django.contrib import admin
from django.urls import path, include
from .views import Home, Signup


urlpatterns = [
    path('', Home, name="home"),
    path('Signup', Signup, name="Signup"),
 
]
