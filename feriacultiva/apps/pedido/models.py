from django.db import models
from apps.producto.models import Producto
from apps.user.models import User
from decimal import Decimal

# Create your models here.
class Pedido(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cliente = models.ForeignKey(User, on_delete=models.CASCADE)
	total = models.DecimalField(max_digits= 8, decimal_places= 2, default = Decimal('1.00'))
	cantidad = models.IntegerField()
	envio = models.BooleanField(default=False)
