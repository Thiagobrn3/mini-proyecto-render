from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'fecha_publicacion')
    list_filter = ('publicado', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')