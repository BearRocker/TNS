from django.db import models
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='games/')

    def __str__(self):
        return self.name

class Tournament(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tier = models.CharField(max_length=20)
    game = models.ForeignKey(Game, models.CASCADE, related_name="game")
    prize = models.IntegerField()
    teams = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    tournaments = models.ForeignKey(Tournament, models.PROTECT, related_name="tournaments", null=True)
    settings = models.CharField(max_length=20)

    def __str__(self):
        return self.login