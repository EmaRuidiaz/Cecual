from django.shortcuts import render
from django.views.generic.list import ListView
from apps.pedido.models import Pedido
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
'''
class ListarPedido(ListView):
	model = Pedido
	template_name = 'Pedido/listarPedidos.html'
'''

def ListarPedido(request):
	context = {}
	context['object_list'] = Pedido.objects.filter(cliente = request.user)

	return render(request, 'Pedido/listarPedidos.html', context)

def DeletePedido(request, pk):

	Pedido.objects.filter(cliente = request.user, pk = pk).delete()
	context = {}
	context['object_list'] = Pedido.objects.filter(cliente = request.user)

	return render(request, 'Pedido/listarPedidos.html', context)

	
