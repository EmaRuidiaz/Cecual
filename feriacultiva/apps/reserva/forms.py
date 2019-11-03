from django.forms import ModelForm
from django import forms
from apps.reserva.models import Reserva

# class ReservaForm(forms.Form): # Tenes que crear el formulario con todos los datos, no te permite trabajar con lo de tu modelo
    
class ReservaForm(ModelForm):  # Te permite trabajar con el formulario de tu modelo

    class Meta:
        model = Reserva
        fields = ['cantidad','envio']
