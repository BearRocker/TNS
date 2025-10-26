from django.shortcuts import render, HttpResponse, redirect
from .models import Game

# Create your views here.

def home(request):
    return render(request, "home.html")

def tournaments(request):
    return render(request, "tournaments.html")

def games(request):
    items = Game.objects.all
    return render(request, "games.html", {"games": items})

def redirect_view(request):
    return redirect('home')