"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.admin import site
from django.urls import include, path
from heronews.views import (SignUpView, 
                            IndexView,
                            ArticleListView, 
                            ArticleDeleteView, 
                            ArticleCreateView, 
                            ArticleDetailView, 
                            ArticleUpdateView,
                            HeroCreateView, 
                            HeroDeleteView, 
                            HeroDetailView, 
                            HeroListView, 
                            HeroUpdateView)

urlpatterns = [
    #Accounts    
    path('accounts/',        include('django.contrib.auth.urls')),
    path(r'admin/', site.urls),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', IndexView.as_view(), name='home'),
    
    #Hero Database
    path('hero/',                HeroListView.as_view(),    name='hero_list'),   
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',   HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
        
    #Article Database
    path('article/',                ArticleListView.as_view(),    name='article_list'),   
    path('article/<str:author>',    ArticleListView.as_view(),    name='my_articles'),   
    path('article/<int:pk>',        ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',             ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/edit',   ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(),  name='article_delete'),
]
