from django import forms
from Cotizador.models import Neumatico

class Buscar(forms.Form):
    modelo = forms.CharField(max_length=10, 
                            widget=forms.TextInput(attrs={'placeholder': 'Buscar...'}))


class NeumaticoForm(forms.ModelForm):
  class Meta:
    model = Neumatico
    fields = ['medida', 'marca', 'modelo']
