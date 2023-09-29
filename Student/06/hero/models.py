from django.db import models

class Superhero(models.Model):
    name = models.CharField(max_length=100, default="Hero Name")
    identity = models.CharField(max_length=100, default="Civilian Name")
    description = models.TextField(default="Description")
    strength = models.CharField(max_length=100, default="Strength")
    weakness = models.CharField(max_length=100, default="Weakness")
    image = models.CharField(max_length=100, default="Image")
