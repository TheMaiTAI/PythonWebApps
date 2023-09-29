from django.contrib import admin

from .models import Superhero

class SuperheroAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(Superhero, SuperheroAdmin)
