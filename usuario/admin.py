from django.contrib import admin

# Register your models here.

from .models import *


class EmpleadoModel(admin.ModelAdmin):

    list_display = (
        '__str__',
        'nombres',
        'apellidos',
        'FechaNacimiento',
        'Cargo',
    )


class AgricultorModel(admin.ModelAdmin):

    list_display = (
        '__str__',
        'nombres',
        'apellidos',
        'FechaNacimiento',
    )


admin.site.register(Empleado, EmpleadoModel)
admin.site.register(Agricultor, AgricultorModel)
