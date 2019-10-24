from django.db import models
from apps.user.models import User
# Create your models here.
class Feriante(models.Model):
	descripcion = models.TextField()
	foto_feriante = models.ImageField(upload_to = 'feriante', null = True)
	delivery = models.BooleanField(default=False, blank=True, null=True)
	encargado = models.OneToOneField(User, on_delete=models.CASCADE)
