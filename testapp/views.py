from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import request
# Create your views here.

def Home(request):
    return render(request,'index.html')



def Signup(request):
    return render(request,'signup.html')