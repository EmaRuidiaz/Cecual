from django import forms
from apps.publicaciones.models import Publicacion
from apps.video.models import Video
from apps.documento.models import Documento

class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['foto', 'titulo', 'contenido']


class VideoForm(forms.ModelForm):
    
    class Meta:
        model = Video
        fields = ['link_video']


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ['pdf']