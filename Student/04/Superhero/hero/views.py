import os
from typing import Any, Dict
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
    path = '/static/images'
    images = os.listdir(path)
    heroes = []
    for i in images:
        fileName = i
        fileName = i[0:-4]
        fileName = fileName.title()
        heroes.append(fileName)

    return heroes
    