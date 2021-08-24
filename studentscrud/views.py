from django.shortcuts import render
from django.views import generic

from django.views import generic

from .models import Estudiante

class StudentsView(generic.ListView):
    template_name = 'studentscrud/estudiantes.html'
    context_object_name = 'lista_de_estudiantes'

    def get_queryset(self):
        """Devuelvo todos los estudiantes"""
        return Estudiante.objects.order_by('nombre')

class StudentView(generic.DetailView):
    model = Estudiante
    template_name = 'studentscrud/estudiante.html'
