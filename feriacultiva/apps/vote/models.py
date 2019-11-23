from django.db import models
from apps.user.models import User
from apps.tema.models import Tema
from apps.comentario.models import Comentario
# Create your models here.

class Vote(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	comentario = models.ForeignKey(Comentario, on_delete = models.CASCADE)
	vote = models.CharField(max_length=2, default="0")    

    #foro = models.ForeignKey(Tema, on_delete = models.CASCADE, related_name = 'comentarioxforo')