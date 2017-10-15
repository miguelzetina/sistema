from django import forms
from .models import Semilla


class SemillaForm(forms.ModelForm):
    class Meta:
        model = Semilla
        fields = [
            'Nombre',
            'CantidadExistente',
            'CantidadPorHectarea',
        ]
        labels = {
            'Nombre':'Nombre de la semilla',
            'CantidadExistente':'Cantidad en Stock (KG)',
            'CantidadPorHectarea' : 'Cantidad por Hectarea (KG)',
        }
