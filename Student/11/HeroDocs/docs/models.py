from django.db import models
from django.db.models.deletion import CASCADE

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    description = models.TextField(default="None")
    image = models.CharField(max_length=200, default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")

class Article(models.Model):
    hero = models.ForeignKey(Superhero, on_delete=CASCADE, editable=False, null=True)
    body = models.TextField(default="")
    title = models.CharField(max_length=100, default="")
    