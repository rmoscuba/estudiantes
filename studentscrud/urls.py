from django.urls import path

from . import views

app_name = 'studentscrud'
urlpatterns = [
    path('', views.StudentsView.as_view(), name='estudiantes'),
    # Estudiantes
    path('estudiante/<int:pk>/', views.StudentView.as_view(), name='estudiante'),
    path('estudiante/nuevo/', views.EstudianteCreateView.as_view(), name='estudiante-nuevo'),
    path('estudiante/<int:pk>/editar', views.EstudianteUpdateView.as_view(), name='estudiante-editar'),
    path('estudiante/<int:pk>/borrar/', views.EstudianteDeleteView.as_view(), name='estudiante-borrar'),
    # Ciudades
    path('ciudades', views.CiudadesView.as_view(), name='ciudades'),
    path('ciudad/<int:pk>/', views.CiudadView.as_view(), name='ciudad'),
    path('ciudad/nuevo/', views.CiudadCreateView.as_view(), name='ciudad-nuevo'),
    path('ciudad/<int:pk>/editar', views.CiudadUpdateView.as_view(), name='ciudad-editar'),
    path('ciudad/<int:pk>/borrar/', views.CiudadDeleteView.as_view(), name='ciudad-borrar'),
]