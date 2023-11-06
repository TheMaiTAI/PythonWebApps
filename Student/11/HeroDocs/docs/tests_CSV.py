import os
from .models import Article, Superhero
from django.test import TestCase
from csv import writer, reader
#-----------------------------------------------#
#Hero Tests
#-----------------------------------------------#
class AddHeroRecordsCSV(TestCase):
    fixtures = Superhero.objects.all()
    def test_add_heroes(self):
        self.assertEqual(len(Superhero.objects.all()), 0)
        
        Superhero.objects.create(name='Iron Man', identity='Tony Stark')
        Superhero.objects.create(name='Deku', identity='Midoriya Izuku')
        num_heroes = len(Superhero.objects.all())
        self.assertEqual(num_heroes, 2)
        
class PrintHeroQueryCSV(TestCase):
    fixtures = Superhero.objects.all()
    def test_print_hero_query(self):
        Superhero.objects.create(name='Iron Man', identity='Tony Stark')
        Superhero.objects.create(name='Deku', identity='Midoriya Izuku')
        
        table = [[h.name, h.identity, h.id] for h in Superhero.objects.all()]
        for row in table:
            print(row[0], row[1], row[2])
            
class HeroExportAsCSV(TestCase):
    def test_export_heroes(self):

        Superhero.objects.create(name='Iron Man', identity='Tony Stark')
        Superhero.objects.create(name='Deku', identity='Midoriya Izuku')
        table = [[h.name, h.identity, h.id] for h in Superhero.objects.all()]
        
        with open('heroes.csv', 'w', newline='') as f:
            writer(f).writerows(table)
            
        file_exists = os.path.exists('heroes.csv')
        self.assertTrue(file_exists)
        
class HeroImportAsCSV(TestCase):
    def test_import_heroes(self):
        with open('heroes.csv') as f:
            return [row for row in reader(f)]
#-----------------------------------------------#
#Article Tests
#-----------------------------------------------#
class AddArticleRecordsCSV(TestCase):
    fixtures = Article.objects.all()
    def test_add_articles(self):
        num_articles = len(Article.objects.all())
        self.assertEqual(num_articles, 0)
        
        Article.objects.create(title='Article 1', body='Article Body 1')
        Article.objects.create(title='Article 2', body='Article Body 2')
        num_articles = len(Article.objects.all())
        self.assertEqual(num_articles, 2)
        
class PrintArticleQueryCSV(TestCase):
    fixtures = Article.objects.all()
    def test_print_article_query(self):
        Article.objects.create(title='Article 1', body='Article Body 1')
        Article.objects.create(title='Article 2', body='Article Body 2')
        
        table = [[a.title, a.body] for a in Article.objects.all()]
        for row in table:
            print(row[0], row[1])
            
class ArticleExportAsCSV(TestCase):
    def test_export_articles(self):

        Article.objects.create(title='Article 1', body='Article Body 1')
        Article.objects.create(title='Article 2', body='Article Body 2')
        
        table = [[a.title, a.body] for a in Article.objects.all()]
        
        with open('articles.csv', 'w', newline='') as f:
            writer(f).writerows(table)
            
        file_exists = os.path.exists('articles.csv')
        self.assertTrue(file_exists)
        
class ArticleImportAsCSV(TestCase):
    def test_import_articles(self):
        with open('articles.csv') as f:
            return [row for row in reader(f)]