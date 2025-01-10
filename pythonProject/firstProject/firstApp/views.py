from django.shortcuts import render 
from django.http import HttpResponse
import datetime 

# Create your views here.

def display(request):
    return HttpResponse("<h1>My Django App </h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b1>Current data and time : </b1>"+str(dt)
    return HttpResponse(s)