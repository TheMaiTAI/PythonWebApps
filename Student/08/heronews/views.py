from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from .models import Superhero, Article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from typing import Any, Dict
from django.shortcuts import redirect, render
import os

#Article Views

class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article
    context_object_name = 'articles'
    
class SortedArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article/sortedlist.html'
    model = Article
    context = Article.objects.all()
    
    def get_page_context(self, request, context=context):
        current_user = self.request.user.pk
        context['my_articles'] = context.filter(author=current_user)
        return context
           
class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article
    context_object_name = 'article'
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article/add.html'
    model = Article
    fields = ['title', 'body']
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/edit.html'
    model = Article
    fields = ['title', 'body']
    
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article/delete.html'
    model = Article
    
    def get_success_url(self):
        return reverse_lazy('article_list')
    
#Hero Views 

class HeroListView(ListView):
    template_name = "hero/list.html"
    model = Superhero
    context_object_name = 'heroes'

class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = 'hero'            

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    
    def get_success_url(self):
        return reverse_lazy("list")
        
#Misc Views

class IndexView(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/acct_add.html"