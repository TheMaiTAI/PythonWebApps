from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero

class HeroDetailView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self,**kwargs):
        context = super(HeroDetailView, self).get_context_data(**kwargs)
        path = self.request.path
        hero = path.replace("/hero/", "")
        context['hero'] = Superhero.objects.filter(slug=hero)        
        return context
        
    
class HeroListView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HeroListView, self).get_context_data(**kwargs)
        context['hero_profiles'] = Superhero.objects.all()
        return context