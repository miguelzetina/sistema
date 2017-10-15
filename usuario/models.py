from django.db import models

# Create your models here.


class Persona(models.Model):
    Nombre = models.CharField(max_length=50,)
    ApMaterno = models.CharField(max_length=50, verbose_name="Apellido materno")
    ApPaterno = models.CharField(max_length=50, verbose_name="Apellido paterno")
    Telefono = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    Direccion = models.CharField(max_length=200)
    FechaNacimiento = models.DateField(
        verbose_name="Fecha de nacimiento",
    )

    def __str__(self):
        return self.Nombre + " " + self.ApMaterno + " " + self.ApPaterno

    def nombres(self):
        return self.Nombre

    def apellidos(self):
        return self.ApMaterno + " " + self.ApPaterno

    class Meta:
        ordering = ["ApMaterno"]


CARGOS = (
    ('GR', 'GERENTE'),
    ('AD', 'ADMINISTRADOR'),
    ('SP', 'SUPERVISOR'),
)


class Empleado(Persona):
    Cargo = models.CharField(max_length=2, choices=CARGOS)

    class Meta:
        verbose_name_plural = "Empleados"


class Agricultor(Persona):
    CURP = models.CharField(max_length=18, unique=True, null=True)
    RFC = models.CharField(max_length=18, unique=True, null=True)

    class Meta:
        verbose_name_plural = "Agricultores"
