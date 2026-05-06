from django import forms
from .models import Restaurante, Plato

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = '__all__'


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'