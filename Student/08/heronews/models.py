from django.urls import reverse, reverse_lazy
from django.db import models
from django.contrib.auth.models import User

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
    heroClass = models.CharField(max_length=200, null=True, default="heroClass")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("hero_detail", kwargs={"pk": self.pk})
    
class Article(models.Model):
    title = models.CharField(max_length=100, default="Article Title")
    body = models.TextField(default="Article Body")
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.pk})