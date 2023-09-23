from django.db import models
from django.urls import reverse

class Superhero(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    heroClass = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("hero_detail", kwargs={"slug": self.slug})