from django import forms
from apps.producto.models import Producto
from apps.feriante.models import Feriante

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ['nombre', 'precio', 'stock', 'foto_producto', 'categoria', 'descripcion']
	


'''


FORMULARIO COMPLETO PARA REVISAR

1- Como obtener el feriante
2- la categoria no me toma como válido


'''