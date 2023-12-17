#C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('redirecionar_para_configuracoes/', views.redirecionar_para_configuracoes, name='redirecionar_para_configuracoes'),
    path('paradas/', views.paradas, name='paradas'),
    path('linhas/', views.linhas, name='linhas'),
    path('resultado_pesquisa/', views.resultado_pesquisa, name='resultado_pesquisa'),
]
