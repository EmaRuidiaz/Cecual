from django.db import models

# Create your models here.
class Publicacion(models.Model):
	foto = models.ImageField()
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()

	def __str__(self):
		return self.titulo