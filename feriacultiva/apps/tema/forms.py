from django import forms
from apps.tema.models import Tema

class TemaForm(forms.ModelForm):

    class Meta:
        model = Tema
        fields = ['titulo','comentario']