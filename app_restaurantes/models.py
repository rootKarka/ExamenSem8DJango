from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='restaurantes/')

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='platos/')

    def __str__(self):
        return self.nombre