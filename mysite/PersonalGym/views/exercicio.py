from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Exercicio


def listar(request):
    exercicios = Exercicio.objects.all()
    return render(request, 'exercicio/listar.html', {'exercicios': exercicios})


def detalhar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    return render(request, 'exercicio/detalhar.html', {'exercicio': exercicio})


ExercicioForm = modelform_factory(Exercicio, fields=('__all__'))


def adicionar(request):
    if request.method == 'POST':
        form = ExercicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('exercicio_listar'))
    else:
        form = ExercicioForm()
    return render(request, 'exercicio/adicionar.html', {'form': form})


def editar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExercicioForm(request.POST, instance=exercicio)
        if form.is_valid():
            form.save()
            return redirect(reverse('exercicio_listar'))
    else:
        form = ExercicioForm(instance=exercicio)
    return render(request, 'exercicio/editar.html', {'form': form})


def apagar(request, pk):
    exercicio = Exercicio.objects.get(pk=pk)
    if request.method == 'POST':
        exercicio.delete()
        return redirect(reverse('exercicio_listar'))
    return render(request, 'exercicio/apagar.html', {'exercicio': exercicio})
