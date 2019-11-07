from django.forms import ModelForm
from django import forms
from apps.pedido.models import Pedido
    
class PedidoForm(ModelForm):  

    class Meta:
        model = Pedido
        fields = ['cantidad','envio']

