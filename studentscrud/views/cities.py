from django.shortcuts import render
from django.views import generic

from django.views import generic

from studentscrud.models import Ciudad

from django.views.generic.edit import FormView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class CiudadesView(generic.ListView):
    template_name = 'studentscrud/ciudades.html'
    context_object_name = 'lista_de_ciudades'

    def get_queryset(self):
        """Devuelvo todos las ciudades"""
        return Ciudad.objects.order_by('nombre')

class CiudadView(generic.DetailView):
    model = Ciudad
    template_name = 'studentscrud/ciudad.html'

class CiudadCreateView(CreateView):
    model = Ciudad
    fields = [
        'nombre'
        ]
    success_url = reverse_lazy('studentscrud:ciudades')

class CiudadUpdateView(UpdateView):
    model = Ciudad
    fields = [
        'nombre'
        ]
    success_url = reverse_lazy('studentscrud:ciudades')

class CiudadDeleteView(DeleteView):
    model = Ciudad
    success_url = reverse_lazy('studentscrud:ciudades')
