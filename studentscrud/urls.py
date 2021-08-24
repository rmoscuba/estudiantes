from django.urls import path

from . import views

app_name = 'studentscrud'
urlpatterns = [
    path('', views.StudentsView.as_view(), name='estudiantes'),
    path('<int:pk>/', views.StudentView.as_view(), name='estudiante'),
]