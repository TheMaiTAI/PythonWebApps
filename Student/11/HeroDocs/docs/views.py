from models import Article
from django.shortcuts import render

def get_articles():
    # data = [a for a in Article.object.all().values()]    
        
    articles = Article.objects.all().values()
    for article in articles:
        print(article)