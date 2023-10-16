from django.urls import reverse, reverse_lazy
from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from .models import Superhero, Article, Author
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

class ArticleListView(ListView):
    template_name = "article/article_list.html"
    model = Article
    context_object_name = "articles"
    
class ArticleDetailView(DetailView):
    template_name = "article/article_detail.html"
    model = Article
    context_object_name = "article"
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/article_add.html"
    model = Article
    fields = "__all__"
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/article_edit.html"
    model = Article
    fields = "__all__"
    
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "article/article_delete.html"
    model = Article
    
    def get_success_url(self):
        return reverse_lazy("hero_list")

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/acct_add.html"