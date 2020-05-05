from django.db import models
from apps.publicaciones.models import Publicacion

class Documento(models.Model):
    pdf = models.FileField(upload_to='documento', blank=True, null=True)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='documentoXpublicacion')

    def __str__(self):
        return str(self.pdf)