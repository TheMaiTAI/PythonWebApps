"""
URL configuration for Superhero project.

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

from django.contrib import admin
from django.urls import path
from hero.views import HeroListView
from hero.views import HeroDetailView

urlpatterns = [
    path('', HeroListView.as_view()),
    path('hero/phantom', HeroDetailView.as_view(name="Phantom")),
    path('hero/shield', HeroDetailView.as_view(name="Shield Hero")),
    path('hero/joker', HeroDetailView.as_view(name="Joker")),
    path('hero/deku', HeroDetailView.as_view(name="Deku")),
    path('hero/corrin', HeroDetailView.as_view(name="Corrin Oskas")),
]