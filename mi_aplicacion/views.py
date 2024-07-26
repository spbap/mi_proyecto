# mi_aplicacion/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'mi_aplicacion/home.html')

def nueva_persona(request):
    return render(request, 'mi_aplicacion/nueva_persona.html')

def nuevo_producto(request):
    return render(request, 'mi_aplicacion/nuevo_producto.html')

def nuevo_pedido(request):
    return render(request, 'mi_aplicacion/nuevo_pedido.html')
