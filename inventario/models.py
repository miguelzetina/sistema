from django.db import models

# Create your models here.


class Semilla(models.Model):
    Nombre = models.CharField(max_length=100)
    CantidadExistente = models.PositiveIntegerField(
        verbose_name="Cantidad existente en KG",
        default=0
    )
    CantidadPorHectarea = models.PositiveIntegerField(
        verbose_name="Cantidad en KG que se movimiento por Hectárea",
        default=0,
    )

    def __str__(self):
        return self.Nombre
