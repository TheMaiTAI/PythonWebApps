from django.test import TestCase
from .models import Superhero, Article, Author

class ArticleDetailPageTest(TestCase):
    def test_page(self):
        page = "http://localhost:8000/article/1"
        response = self.client.get(page)
        self.assertEqual(response.status_code, 302)
        
class ArticleAuthorTest(TestCase):
    fixtures = ['data.json']
    
    def get_author(self):
        user = self.client.force_login(user)
        author = Article.objects.get(author=user)
        self.assertEqual(author, 'hulk')
        