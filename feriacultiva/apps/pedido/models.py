from django.db import models
from apps.producto.models import Producto
from apps.user.models import User

# Create your models here.
class Pedido(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	envio = models.BooleanField(default=False)
