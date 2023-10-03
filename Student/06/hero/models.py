from django.urls import reverse
from django.db import models

class Superhero(models.Model):
    class Meta:
        db_table = 'hero_database'
    name = models.CharField(max_length=100, default="Hero Name")
    identity = models.CharField(max_length=100, default="Civilian Name")
    description = models.TextField(default="Description")
    strength = models.CharField(max_length=100, default="Strength")
    weakness = models.CharField(max_length=100, default="Weakness")
    image = models.CharField(max_length=100, default="Image")
    slug = models.SlugField(null=False, unique=True, default="hero-name")
    heroClass = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("hero_detail", kwargs={"slug": self.slug, "key": self.pk})