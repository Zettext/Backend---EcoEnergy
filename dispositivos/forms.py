from django import forms
from .models import Dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'categoria', 'zona', 'consumo_maximo', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'consumo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }