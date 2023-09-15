from django.urls import path
from hero.views import HeroFirstDetailView, HeroSecondDetailView, HeroThirdDetailView, HeroListView

urlpatterns = [
    path('',            HeroListView.as_view()),
    path('shield',       HeroFirstDetailView.as_view()),
    path('ghost',       HeroSecondDetailView.as_view()),
    path('thief',       HeroThirdDetailView.as_view()),
]