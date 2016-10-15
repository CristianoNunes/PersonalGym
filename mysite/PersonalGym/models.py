from django.db import models
from django.utils import timezone


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=9)


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField()


class Serie(models.Model):
    quantidade = models.IntegerField()
    repeticao = models.IntegerField()


class Treino(models.Model):
    nome = models.CharField(max_length=100)
    data_incio = models.DateField(default=timezone.now)
    data_fim = models.DateField()
    aluno = models.ForeignKey(Aluno)
    exercicio = models.ForeignKey(Exercicio)
    serie = models.ForeignKey(Serie)
