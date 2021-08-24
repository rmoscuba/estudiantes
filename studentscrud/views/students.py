from django.shortcuts import render
from django.views import generic

from django.views import generic

from studentscrud.models import Estudiante

from django.views.generic.edit import FormView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class StudentsView(generic.ListView):
    template_name = 'studentscrud/estudiantes.html'
    context_object_name = 'lista_de_estudiantes'

    def get_queryset(self):
        """Devuelvo todos los estudiantes"""
        return Estudiante.objects.order_by('nombre')

class StudentView(generic.DetailView):
    model = Estudiante
    template_name = 'studentscrud/estudiante.html'

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = [
        'nombre',
        'sexo',
        'email',
        'fecha_nacimiento',
        'ciudad_nacimiento',
        'grupo'
        ]
    success_url = reverse_lazy('studentscrud:estudiantes')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = [
        'nombre',
        'sexo',
        'email',
        'fecha_nacimiento',
        'ciudad_nacimiento',
        'grupo'
        ]
    success_url = reverse_lazy('studentscrud:estudiantes')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('studentscrud:estudiantes')