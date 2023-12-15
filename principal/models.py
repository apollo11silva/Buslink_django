# C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\principal\models.py
from django.db import models

class Linha(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Parada(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Horario(models.Model):
    linha = models.ForeignKey(Linha, on_delete=models.CASCADE)
    horario = models.TimeField()
    parada = models.ForeignKey(Parada, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.linha} - {self.parada} - {self.horario}'

