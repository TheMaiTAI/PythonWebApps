from django.shortcuts import render
from django.views.generic import TemplateView

class ListView(TemplateView):
    template_name = "hero/index.html"
