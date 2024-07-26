# mi_proyecto/urls.py

from django.contrib import admin
from django.urls import path
from mi_aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('nueva_persona/', views.nueva_persona, name='nueva_persona'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('nuevo_pedido/', views.nuevo_pedido, name='nuevo_pedido'),
]
