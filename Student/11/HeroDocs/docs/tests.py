from fileinput import filename
from pathlib import Path
from .models import Article
from django.test import TestCase
from json import dump

#Misc Tests

class CheckDatabase(TestCase):
    fixtures = Article.objects.all()
    num_articles = len(Article.objects.all())
    def test_database_is_empty(self, num = num_articles):
        print(num)
        self.assertEquals(num, 0)

#JSON Tests
# class AddArticlesJSON(TestCase):
#     data = [a for a in Article.object.all().values()]
    