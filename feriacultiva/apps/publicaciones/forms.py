from django import forms
from apps.publicaciones.models import Publicacion
from apps.video.models import Video

class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['foto', 'titulo', 'contenido']


class VideoForm(forms.ModelForm):
    
    class Meta:
        model = Video
        fields = ['link_video']
