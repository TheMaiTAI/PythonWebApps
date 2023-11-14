from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse, reverse_lazy

class Investigator(models.Model):
    name = models.CharField(max_length=100, default="Name")
    user = models.OneToOneField(User, on_delete=CASCADE, editable=False, null=True)
    
    def __str__(self):
        return self.user.username
    
    @staticmethod
    def get_me(user):
        return Investigator.objects.get_or_create(user=user)[0]
    
def get_upload(instance, filename):
    # if instance.folder:
    #     return f'images/{instance.folder}/{filename}'
    return f'images/{filename}'

class Superhero(models.Model):
    
    name = models.CharField(max_length=100, default="")
    identity = models.CharField(max_length=100, default="")
    description = models.TextField(default="")
    strength = models.CharField(max_length=100, default="")
    weakness = models.CharField(max_length=100, default="")
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)
    investigator = models.ForeignKey(Investigator, on_delete=CASCADE, editable=False, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("hero_detail")
    
class Article(models.Model):
    hero = models.ForeignKey(Superhero, on_delete=CASCADE, editable=False, null=True)
    body = models.TextField(default="")
    investigator = models.ForeignKey(Investigator, on_delete=CASCADE, editable=False, null=True)
    #order = models.OrderBy()
    title = models.CharField(max_length=100, default="")