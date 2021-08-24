from django.shortcuts import render
from django.views import generic

from django.views import generic

from studentscrud.models import Grupo

from django.views.generic.edit import FormView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class GruposView(generic.ListView):
    template_name = 'studentscrud/Grupos.html'
    context_object_name = 'lista_de_grupos'

    def get_queryset(self):
        """Devuelvo todos las Grupoes"""
        return Grupo.objects.order_by('nombre')

class GrupoView(generic.DetailView):
    model = Grupo
    template_name = 'studentscrud/Grupo.html'

class GrupoCreateView(CreateView):
    model = Grupo
    fields = [
        'nombre',
        'profesor_guia'
        ]
    success_url = reverse_lazy('studentscrud:grupos')

class GrupoUpdateView(UpdateView):
    model = Grupo
    fields = [
        'nombre',
        'profesor_guia'
        ]
    success_url = reverse_lazy('studentscrud:grupos')

class GrupoDeleteView(DeleteView):
    model = Grupo
    success_url = reverse_lazy('studentscrud:grupos')
