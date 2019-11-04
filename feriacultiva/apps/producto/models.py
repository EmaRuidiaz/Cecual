from django.db import models
from apps.categoria.models import Categoria
from apps.feriante.models import Feriante
# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=100)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField()
	foto_producto = models.ImageField(upload_to = 'productos', null = True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productosXcategoria')
	feriante = models.ForeignKey(Feriante, on_delete=models.CASCADE, related_name='productosXferiante')

	def __str__(self):
		return self.nombre