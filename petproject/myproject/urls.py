from django.urls import path

from . import views

urlpatterns =[
    path("", views.redirect_view, name="redirect_view"),
    path("home", views.home, name="home"),
    path("tournaments", views.tournaments, name="tournaments"),
    path("games", views.games, name="games")
]