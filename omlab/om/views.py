from django.shortcuts import render
from django.http import HttpResponse
from om import models
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return (render(request,"om/index.html"))

def display(request):
    if request.method=="POST":
        om = models.OmLab.objects.filter(passcode=request.POST['passcode'])
        if om:
            res=render(request,"om/index_display.html",{'om':om})
            return(res)
        else:
            error="Enter a valid  name and passcode"
    return (render(request,"om/index.html",{"error":error}))
