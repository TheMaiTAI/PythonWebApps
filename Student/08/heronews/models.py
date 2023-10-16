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
        return reverse("hero_detail", kwargs={"pk": self.pk})
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'

    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    @property
    def articles(self):
        return Article.objects.filter(author=self)

    @staticmethod
    def get_me(user):
        return Author.objects.get_or_create(user=user)[0]
    
    
class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse_lazy('article_detail', args=[str(self.id)])