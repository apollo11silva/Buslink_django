# C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\views.py
from django.shortcuts import render, redirect
from .models import Parada, Linha



def home(request):
    return render(request, 'home.html')

def configuracoes(request):
    return render(request, 'configuracoes.html')

def redirecionar_para_configuracoes(request):
    return redirect('configuracoes')

def paradas(request):
    paradas = Parada.objects.all()  # Obtém todas as paradas do banco de dados
    return render(request, 'paradas.html', {'paradas': paradas})

def linhas(request):
    linhas = Linha.objects.all()
    return render(request, 'linhas.html', {'linhas': linhas})