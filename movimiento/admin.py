from django.contrib import admin

# Register your models here.

from .models import *


class EntregaAAgricultorAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'HectareasAPlantar',
        'SemillasDadas',
        'TipoSemilla',
        'NombreAgricultor',
        'FechaEntrega',
    )


admin.site.register(EntregaAAgricultor, EntregaAAgricultorAdmin)
