from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurante
from .forms import RestauranteForm

def lista_restaurantes(request):
    data = Restaurante.objects.all()
    return render(request, 'restaurantes/lista.html', {'data': data})


def crear_restaurante(request):
    form = RestauranteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'restaurantes/form.html', {'form': form})


def editar_restaurante(request, id):
    obj = get_object_or_404(Restaurante, id=id)
    form = RestauranteForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'restaurantes/form.html', {'form': form})


def eliminar_restaurante(request, id):
    obj = get_object_or_404(Restaurante, id=id)
    obj.delete()
    return redirect('lista')