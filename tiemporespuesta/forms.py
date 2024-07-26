from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ['letra_1', 'tiempo_1', 'letra_2', 'tiempo_2', 'letra_3', 'tiempo_3', 'letra_4', 'tiempo_4', 'letra_5', 'tiempo_5']
        widgets = {
            'letra_1': forms.TextInput(attrs={'readonly': 'readonly'}),
            'letra_2': forms.TextInput(attrs={'readonly': 'readonly'}),
            'letra_3': forms.TextInput(attrs={'readonly': 'readonly'}),
            'letra_4': forms.TextInput(attrs={'readonly': 'readonly'}),
            'letra_5': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
