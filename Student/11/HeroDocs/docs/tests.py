import os
from pathlib import Path
from .models import Article, Superhero
from django.test import TestCase
from json import dump, loads

#Misc Tests

class CheckDatabase(TestCase):
    fixtures = Article.objects.all()
    num_articles = len(Article.objects.all())
    def test_database_is_empty(self, num = num_articles):
        print(num)
        self.assertEquals(num, 0)

#JSON Tests
#Heroes
class AddHeroesJSON(TestCase):
    fixtures = Superhero.objects.all()
    def test_add_heroes(self):
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 0)
        
        Superhero.objects.create(name="Iron Man", identity="Tony Stark")
        Superhero.objects.create(name="Deku", identity="Midoriya Izuku")
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 2)
        
class PrintHeroQueryJSON(TestCase):    
    def test_print_hero_query(self):
        heroes = Superhero.objects.all().values()
        for hero in heroes:
            print(hero)
    
class HeroExportAsJSON(TestCase):
    def test_export_heroes(self):
        data = [h for h in Superhero.objects.all().values()]
        with open("heroes.json", "w") as f:
            dump(data, f, indent=4)
            
        file_exists = os.path.exists("heroes.json")
        self.assertTrue(file_exists)
        os.remove("heroes.json")
        
class HeroImportAsJSON(TestCase):
    def test_import_heroes(self):
        data = [h for h in Superhero.objects.all().values()]
        
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 0)
        Superhero.objects.create(name="Iron Man", identity="Tony Stark")
        Superhero.objects.create(name="Deku", identity="Midoriya Izuku")
        
        with open("heroes.json", "w") as f:
            dump(data, f, indent=4)
            
        path = Path("heroes.json")
        if path.exists():
            objects = loads(path.read_text())
        for o in objects:
            Superhero.objects.get_or_create(**o)
            
        num_heroes = len(Superhero.objects.all())
        self.assertNotEqual(num_heroes, 0)
        os.remove("heroes.json")

#Articles
class AddArticlesJSON(TestCase):
    fixtures = Article.objects.all()
    def test_add_articles(self):
        num_articles = len(Article.objects.all())
        self.assertEqual(num_articles, 0)
        
        Article.objects.create(title="Article 1", body="Article Body 1")
        Article.objects.create(title="Article 2", body="Article Body 2")
        num_articles = len(Article.objects.all())
        self.assertEqual(num_articles, 2)
        
class PrintArticleQueryJSON(TestCase):    
    def test_print_article_query(self):
        articles = Article.objects.all().values()
        for article in articles:
            print(article)
    
class ArticleExportAsJSON(TestCase):
    def test_export_articles(self):
        data = [a for a in Article.objects.all().values()]
        with open("articles.json", "w") as f:
            dump(data, f, indent=4)
            
        file_exists = os.path.exists("articles.json")
        self.assertTrue(file_exists)
        os.remove("articles.json")
        
class ArticleImportAsJSON(TestCase):
    def test_import_articles(self):
        data = [a for a in Article.objects.all().values()]
        
        num_articles = len(Article.objects.all())
        self.assertEqual(num_articles, 0)
        Article.objects.create(title="Article 1", body="Article Body 1")
        Article.objects.create(title="Article 2", body="Article Body 2")
        
        with open("articles.json", "w") as f:
            dump(data, f, indent=4)
            
        path = Path("articles.json")
        if path.exists():
            objects = loads(path.read_text())
        for o in objects:
            Article.objects.get_or_create(**o)
            
        num_articles = len(Article.objects.all())
        self.assertNotEqual(num_articles, 0)
        os.remove("articles.json")