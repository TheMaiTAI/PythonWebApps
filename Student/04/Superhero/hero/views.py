import os
from typing import Any, Dict

from Superhero.settings import STATICFILES_DIRS
from Superhero.settings import BASE_DIR
from django.shortcuts import render
from pathlib import Path
from django.views.generic import TemplateView


class HeroListView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        
        return dict(heroes=hero_list())
    


class HeroDetailView(TemplateView):
    template_name = "hero.html"
    name = "hero"
    
    def get_context_data(self, **kwargs):
        name = kwargs['name']
        imgName = name.lower()
        image = f'/static/images/{imgName}'
        heroName = name.title()
        className = name.lower()
        className = className.replace(" ", "")
        
        return {
            'heroName' : heroName,
            'image': image,
            'heroClass': className
            }

def hero_list():
    
    fileName = ""
    heroes = Path('static/images').iterdir()
    heroes = [f for i, f in enumerate(heroes)]
    

    return heroes
    