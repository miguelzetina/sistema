from django.contrib import admin

# Register your models here.

from .models import *


class SemillaAdmin(admin.ModelAdmin):

    list_display = (
        'Nombre',
        'CantidadExistente',
        'CantidadPorHectarea'
    )


admin.site.register(Semilla, SemillaAdmin)
