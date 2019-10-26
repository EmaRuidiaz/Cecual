from django import forms
from apps.producto.models import Producto
from apps.feriante.models import Feriante

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto
		
		#feriante = Feriante.objects.get(encargado = self.request.user)
		fields = ['nombre', 'precio', 'stock', 'foto_producto', 'categoria', 'feriante']
	
	def get_queryset(self):
		# pass "user" keyword argument with the current user to your form
		kwargs = super(ProductoForm, self).get_form_kwargs()
		categoria = self.request.GET.get('categoria', None)
		kwargs['feriante'] = Feriante.objects.get(encargado = self.request.user)
		return kwargs

'''


FORMULARIO COMPLETO PARA REVISAR

1- Como obtener el feriante
2- la categoria no me toma como válido


'''