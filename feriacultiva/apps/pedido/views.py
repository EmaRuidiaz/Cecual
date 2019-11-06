from django.shortcuts import render
from django.views.generic.list import ListView
from apps.pedido.models import Pedido
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class ListarPedido(ListView):
	model = Pedido
	template_name = 'Pedido/listarPedidos.html'

	
