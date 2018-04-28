from django import forms
from .models import TIPOS


class PersonajeForm(forms.Form):
    """
    Formulario de los Personajes
    """
    nombre = forms.CharField(widget=forms.TextInput(attrs={
        "class": "validate", "placeholder": "Escribe aquí el Nombre del personaje",
        "id":"nombre"
        }))
    tipo_personaje = forms.ChoiceField(choices=TIPOS)
    imagen = forms.ImageField()
    descripcion = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'materialize-textarea', "placeholder": "Describe tu Personaje",}))
    