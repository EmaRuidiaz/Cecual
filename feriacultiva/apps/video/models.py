from django.db import models
from apps.publicaciones.models import Publicacion

class Video(models.Model):
    link_video = models.CharField(max_length = 400, null=True, blank=True)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='videosXpublicacion')

    def __str__(self):
        return str(self.link_video)
