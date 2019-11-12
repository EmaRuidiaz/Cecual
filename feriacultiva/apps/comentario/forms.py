from django import forms
from apps.comentario.models import Comentario

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['comentario']