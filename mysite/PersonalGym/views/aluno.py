from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Aluno


def listar(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/listar.html', {'alunos': alunos})


def detalhar(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    return render(request, 'aluno/detalhar.html', {'aluno': aluno})


AlunoForm = modelform_factory(Aluno, fields=('__all__'))


def adicionar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('aluno_listar'))
    else:
        form = AlunoForm()
    return render(request, 'aluno/adicionar.html', {'form': form})


def editar(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect(reverse('aluno_listar'))
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'aluno/editar.html', {'form': form})


def apagar(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect(reverse('aluno_listar'))
    return render(request, 'aluno/apagar.html', {'aluno': aluno})
