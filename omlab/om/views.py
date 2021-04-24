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

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request)
            data = models.OmLab.objects.all()
            return (render(request, "om/show_all.html",{'data':data}))
        return(res)
    res=render(request, "om/login_lab.html")
    return(res)

