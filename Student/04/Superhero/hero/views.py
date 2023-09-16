from django.shortcuts import render
from django.views.generic import TemplateView

class HeroListView(TemplateView):
    template_name = "heroes.html"
