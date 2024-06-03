from django.db import models


class Videogame(models.Model):
    title = models.CharField(max_length=100, blank=False, default=None)
    game_studio = models.CharField(max_length=100, blank=False, default=None)
    creator = models.CharField(max_length=50, blank=False, default=None)
    genre = models.CharField(max_length=50, default=None)
    description = models.TextField(max_length=400,blank=False, default=None)
    published_date = models.DateTimeField(default=None, auto_now_add=True)
    steam_price = models.FloatField(max_length=50, default=None)
    
    