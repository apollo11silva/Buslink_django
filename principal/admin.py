#C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\admin.py
from django import forms
from .models import Linha, Parada, Horario, Local, Favorito
from django.contrib import admin

@admin.register(Linha)
class LinhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')

@admin.register(Parada)
class ParadaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao')

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('linha', 'horario', 'parada')

@admin.register(Local)
class LocaisAdmin(admin.ModelAdmin):
    list_display = ('nome',)    

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('nome',)       

