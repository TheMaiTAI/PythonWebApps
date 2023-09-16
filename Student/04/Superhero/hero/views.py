from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView

class HeroListView(TemplateView):
    template_name = "heroes.html"

class HeroDetailView(TemplateView):
    template_name = "hero.html"
    name = "hero"
    
    def get_context_data(self, **kwargs):
        name = self.name
        
        return {'hero' : name}