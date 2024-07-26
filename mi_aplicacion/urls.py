from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Asegúrate de que 'home' sea el nombre correcto de tu vista
    # Agrega aquí más rutas según tus vistas
]
