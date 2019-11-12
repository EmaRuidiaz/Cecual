from django.db import models
from apps.user.models import User

# Create your models here.

class Tema(models.Model):
    creador = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'temaxuser')
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    cantidad_respuesta = models.IntegerField(default = 0)
    comentario = models.TextField(max_length = 500)
    titulo = models.CharField(max_length =100)

    def __str__(self):
        return self.titulo
