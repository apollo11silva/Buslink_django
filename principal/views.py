# C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\views.py
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def configuracoes(request):
    return render(request, 'configuracoes.html')

def redirecionar_para_configuracoes(request):
    return redirect('configuracoes')
