from django.contrib import admin

from .models import Superhero

class SuperheroAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    

admin.site.register(Superhero, SuperheroAdmin)
