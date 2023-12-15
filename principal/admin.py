#C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\admin.py
from django import forms
from .models import Linha, Parada, Horario
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

