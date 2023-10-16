from django.test import TestCase, SimpleTestCase
from .models import Superhero, Article, Author

class HeroNewsAppTest(SimpleTestCase):
        
    def test_page(self):
        page = "https://tlee-proj08-z9ku8.ondigitalocean.app/article/"
        response = self.client.get(page)
        self.assertEqual(response.status_code, 200)