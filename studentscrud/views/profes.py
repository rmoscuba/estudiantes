from django.shortcuts import render
from django.views import generic

from django.views import generic

from studentscrud.models import Profesor as Profe

from django.views.generic.edit import FormView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ProfesView(generic.ListView):
    template_name = 'studentscrud/profesores.html'
    context_object_name = 'lista_de_profes'

    def get_queryset(self):
        """Devuelvo todos las Profesores"""
        return Profe.objects.order_by('nombre')

class ProfeView(generic.DetailView):
    model = Profe
    template_name = 'studentscrud/profesor.html'

class ProfeCreateView(CreateView):
    model = Profe
    fields = [
        'nombre'
        ]
    success_url = reverse_lazy('studentscrud:profes')

class ProfeUpdateView(UpdateView):
    model = Profe
    fields = [
        'nombre'
        ]
    success_url = reverse_lazy('studentscrud:profes')

class ProfeDeleteView(DeleteView):
    model = Profe
    success_url = reverse_lazy('studentscrud:profes')
