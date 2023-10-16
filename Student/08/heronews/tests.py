from django.test import TestCase, SimpleTestCase
from .models import Superhero, Article, Author

class HeroNewsAppTest(TestCase):
    fixtures = ['newsdata.json']
    
    def test_with_data(self):
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 0)