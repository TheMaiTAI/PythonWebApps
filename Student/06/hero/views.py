from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from .models import Superhero
import os

class IndexView(TemplateView):
    template_name = "index.html"

class HeroListView(ListView):
    template_name = "hero/list.html"
    model = Superhero
    context_object_name = 'heroes'
    
    def get_context_data(self, name=context_object_name, **kwargs):
        context = super(HeroListView, self).get_context_data(**kwargs)
        context[name] = Superhero.objects.all();
        return context;

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero_details'
        
    def get_context_data(self, name=context_object_name, **kwargs):                        
        context = super(HeroDetailView, self).get_context_data(**kwargs)
        path = Superhero.get_absolute_url(self)
        key = path["key"]
        context[name] = Superhero.objects.filter(pk=key)
        return context;

class HeroCreateView(CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'

class HeroUpdateView(UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

class HeroDeleteView(DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    
