from django.db import models

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=30)
	foto = models.ImageField(upload_to = 'categoria')

	def __str__(self):
		return self.nombre