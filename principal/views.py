# C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\views.py
from django.shortcuts import render, redirect
from .models import Parada, Linha, Favorito



def home(request):
    favoritos = Favorito.objects.all()
    return render(request, 'home.html',  {'favoritos': favoritos})

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



def resultado_pesquisa(request):
    if request.method == 'POST':
        local_partida = request.POST.get('local_partida')
        destino = request.POST.get('destino')

        # Aqui você pode realizar qualquer processamento necessário com os dados

        # Renderize a página de resultado com os dados processados
        return render(request, 'resultado_pesquisa.html', {'local_partida': local_partida, 'destino': destino})
    else:
        # Trate o caso de acesso direto à URL sem dados de pesquisa
        return render(request, 'erro_pesquisa.html')