from django.urls import reverse, reverse_lazy
from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from .models import Superhero
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    template_name = "index.html"

class HeroListView(ListView):
    template_name = "hero/hero_list.html"
    model = Superhero
    context_object_name = 'heroes'

class HeroDetailView(DetailView):
    template_name = 'hero/hero_detail.html'
    model = Superhero
    context_object_name = 'hero'            

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/hero_add.html"
    model = Superhero
    fields = '__all__'

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/hero_edit.html"
    model = Superhero
    fields = '__all__'

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/hero_delete.html'
    
    def get_success_url(self):
        return reverse_lazy("hero_list")
        
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/acct_add.html"
    
