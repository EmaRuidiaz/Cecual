from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from apps.producto.models import Producto
from apps.categoria.models import Categoria
from apps.evento.models import Evento
from apps.pedido.models import Pedido
from apps.user.models import User
from django.views.generic.list import ListView
from django.db.models import Sum



class Inicio(ListView):
	model = Producto
	template_name = 'start.html'
	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		productos = Producto.objects.all().order_by('-id')[:9]
		context['Recientes'] = productos

		categorias = Categoria.objects.all() 
		context['Categorias'] = categorias
		
		eventos = Evento.objects.all() 
		context['EventoInfo'] = eventos


		if self.request.user.is_authenticated:
			pedidos = Pedido.objects.filter(cliente = self.request.user).aggregate(Sum('cantidad'))
			context['Pedido'] = pedidos

		return context







@login_required
def  Administrador(request):
	user = User.objects.get(username = request.user)
	if user.is_superuser == True:
		return render(request, 'administrador.html')
	else:
		return redirect(reverse('login'))


