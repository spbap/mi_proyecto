from django.db import models
from django.utils import timezone

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)  # Sin default
    cantidad = models.IntegerField(default=0)  # Default para evitar problemas

    def __str__(self):
        return f'Pedido de {self.persona} para {self.producto}'
