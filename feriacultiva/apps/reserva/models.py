from django.db import models
from apps.user.models import User
from apps.feriante.models import Feriante
from apps.producto.models import Producto
from decimal import Decimal

# Create your models here.

class Reserva(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.PROTECT, related_name = 'reservaxproducto')
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits= 8, decimal_places= 2, default = Decimal('1.00'))
    user = models.ForeignKey(User, on_delete = models.PROTECT, related_name = 'reservaxuser')
    envio = models.BooleanField(default = False, blank = True)