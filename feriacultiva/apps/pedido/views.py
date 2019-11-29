from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from apps.pedido.models import Pedido
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from apps.pedido.forms import PedidoForm
from decimal import Decimal
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# class ListarPedido(ListView):
# 	model = Pedido
# 	template_name = 'Pedido/listarPedidos.html'


def ListarPedido(request):
	context = {}
	
	if request.user.is_authenticated:
		
		context['object_list'] = Pedido.objects.filter(cliente = request.user)
		clave = request.POST.get('Confirmar')
		print(clave)
		try:
			p = Pedido.objects.get(pk = clave)
			print(p)
		except Pedido.DoesNotExist:
			print('nada')
		
		if request.POST.get:
			form = PedidoForm(request.POST)
			if form.is_valid():
				cant = request.POST.get('cantidad')
				total = Decimal(cant) * p.producto.precio
				p.cantidad = cant
				p.total = total
				p.save()
		context['total'] = Pedido.objects.filter(cliente = request.user).aggregate(Sum('total')) # Trae el precio total de todos los pedidos
	else:
		print('no esta registrado')
		return redirect(reverse('producto:ListarProducto'))
	pedidos = Pedido.objects.filter(cliente = request.user).aggregate(Sum('cantidad'))
	context['Pedido'] = pedidos
	return render(request, 'Pedido/listarPedidos.html', context)
	

def DeletePedido(request, pk):

	Pedido.objects.filter(cliente = request.user, pk = pk).delete()
	context = {}
	context['object_list'] = Pedido.objects.filter(cliente = request.user)

	return render(request, 'Pedido/listarPedidos.html', context)