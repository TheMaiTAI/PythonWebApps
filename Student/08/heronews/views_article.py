from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin

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