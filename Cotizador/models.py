from django.db import models

class Neumatico(models.Model):
    medida = models.CharField(max_length=12)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    stock = models.IntegerField()
    precio = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.medida}, {self.marca}, {self.modelo}, {self.stock}, {self.precio}"

