from django.db import models
from apps.categoria.models import Categoria
# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField()
	foto_producto = models.ImageField(upload_to = 'productos', null = True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productosXcategoria')
	feriante = models.ForeignKey(Feriante, on_delete=models.CASCADE, related_name='productosXferiante')