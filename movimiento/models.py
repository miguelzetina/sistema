from django.db import models
from inventario.models import Semilla
from usuario.models import Agricultor
# Create your models here.


class EntregaAAgricultor(models.Model):
    FechaEntrega = models.DateField(
        verbose_name="Fecha de movimiento",
        auto_now=True
    )
    HectareasAPlantar = models.PositiveIntegerField(verbose_name="Hectareas a plantar")
    SemillasDadas = models.PositiveIntegerField(
        verbose_name="KG de semillas dadas",
        default=1,
    )
    TipoSemilla = models.ForeignKey(
        Semilla,
        verbose_name="Tipo de semillas que se darán",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    NombreAgricultor = models.ForeignKey(
        Agricultor,
        default=2,
        verbose_name="Agricultor al que se le darán las semillas",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.SemillasDadas) + " KG de " + str(self.TipoSemilla) + " - " + str(self.NombreAgricultor)

    class Meta:
        ordering = ["-FechaEntrega"]
        verbose_name_plural = "Entregas a agricultores"














