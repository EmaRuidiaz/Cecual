from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.producto.models import Producto
from apps.categoria.models import Categoria
from apps.pedido.models import Pedido
from django.views.generic.list import ListView



class Inicio(ListView):
	model = Producto
	template_name = 'start.html'
	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		productos = Producto.objects.all().order_by('-id')[:9]
		context['Recientes'] = productos

		categorias = Categoria.objects.all() 
		context['Categorias'] = categorias

		if self.request.user.is_authenticated:
			pedidos = Pedido.objects.filter(cliente = self.request.user)
			context['Pedido'] = pedidos

		return context







@login_required
def  Administrador(request):
	return render(request, 'administrador.html')


