from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect
import sys
sys.path.append("..")
from myproject.models import User

# Create your views here.

def login(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        if username and password:
            username_exist = User.objects.filter(login=username)
            if username_exist:
                if User.objects.get(login=username).password == password:
                    print(username, password)
                else:
                    error = "Password is incorrect"
            else:
                error = "username is already taken,try another"
        else:
            error = "all fields are required"
    return render(request, "login.html", {'error': error})

def register(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password-confirm")
        print(username, password, password_confirm)
        if password == password_confirm:
            new_user = User.objects.create(login=username, password=password, settings='1 hour')
        else:
            error = "Password are not the same"
    return render(request, "register.html", {'error': error})

def registration(request):
    pass
