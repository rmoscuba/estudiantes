from django.urls import path

from . import views

app_name = 'studentscrud'
urlpatterns = [
    path('', views.StudentsView.as_view(), name='estudiantes'),
    path('estudiante/<int:pk>/', views.StudentView.as_view(), name='estudiante'),
    path('estudiante/nuevo/', views.EstudianteCreateView.as_view(), name='estudiante-nuevo'),
    path('estudiante/<int:pk>/editar', views.EstudianteUpdateView.as_view(), name='estudiante-editar'),
    path('estudiante/<int:pk>/borrar/', views.EstudianteDeleteView.as_view(), name='estudiante-borrar'),
]