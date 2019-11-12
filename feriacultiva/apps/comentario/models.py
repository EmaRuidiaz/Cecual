from django.db import models
from apps.user.models import User
from apps.tema.models import Tema

# Create your models here.

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comentarioxuser')
    foro = models.ForeignKey(Tema, on_delete = models.CASCADE, related_name = 'comentarioxforo')
    fecha_comentario = models.DateTimeField(auto_now_add = True)
    comentario = models.CharField(max_length = 500)
