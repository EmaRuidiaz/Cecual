from django.db import models

# Create your models here.
class Evento(models.Model):
	foto = models.ImageField(upload_to = 'evento')
	titulo = models.CharField(max_length=200)
	dia = models.CharField(max_length=20)
	f_inicio = models.DateTimeField()
	f_finalizacion = models.DateTimeField()
	descripcion = models.TextField()
	direccion = models.CharField(max_length=200)

	def __str__(self):
		return self.titulo 
