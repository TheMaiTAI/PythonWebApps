from django.test import TestCase
from hero.models import Investigator, Superhero, Article

class TestInvestigatorData(TestCase):
    def test_investigator(self):
        self.assertEqual(len(Investigator.objects.all()), 0)
        Investigator.objects.create(name='Test Johnson')
        Investigator.objects.create(name='Sally Johnson')
        self.assertEqual(len(Investigator.objects.all()), 2)
        
        i = Investigator.objects.get(pk=2)
        self.assertEqual(i.name, 'Sally Johnson')
        
        i.name = "Sally Stone"
        i.save()
        self.assertEqual(i.name, 'Sally Stone')
        
        i.delete()
        self.assertEqual(len(Investigator.objects.all()), 1)

# class TestInvestigatorViews(TestCase):
#     #test contents
    
class TestSuperheroData(TestCase):
    def test_hero(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        Superhero.objects.create(name='Iron Man')
        Superhero.objects.create(identity='Bruce Wayne')
        self.assertEqual(len(Superhero.objects.all()), 2)
        
        i = Superhero.objects.get(pk=1)
        i.identity = "Tony Stark"
        i.save()
        self.assertEqual(i.identity, 'Tony Stark')
        
        i.delete()
        self.assertEqual(len(Superhero.objects.all()), 1)
    
# class TestSuperheroViews(TestCase):
#     #test contents
    
class TestArticleData(TestCase):
    def test_article(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title='Title 1')
        Article.objects.create(title='Title 2')
        self.assertEqual(len(Article.objects.all()), 2)
        
        a = Article.objects.get(pk=2)
        self.assertEqual(a.title, 'Title 2')
        
        a.title = "Test Article"
        a.save()
        self.assertEqual(a.title, 'Test Article')
        
        a.delete()
        self.assertEqual(len(Article.objects.all()), 1)
        
    
# class TestArticleViews(TestCase):
#     #test contents