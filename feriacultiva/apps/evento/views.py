from django.shortcuts import render
from django.views.generic.list import ListView
from apps.evento.models import Evento
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
class ListarEventos(ListView):
	model = Evento
	template_name = 'evento/listarEventos.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			pedidos = Pedido.objects.filter(cliente = self.request.user).aggregate(Sum('cantidad'))
			context['Pedido'] = pedidos

		return context

class ListarEventosAdmin(ListView):
	model = Evento
	template_name = 'evento/listarEventosAdmin.html'

class AgregarEvento(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Evento
	template_name = 'Evento/NuevoEvento.html'
	success_url = reverse_lazy('evento:listarEventosAdmin')
	fields = '__all__'

class DetalleEvento(DetailView):
	model = Evento
	template_name = 'Evento/detalleEvento.html'

class ModificarEvento(LoginRequiredMixin,UpdateView):
	model = Evento
	template_name = 'Evento/agregarEvento.html'
	success_url = reverse_lazy('evento:listarEventosAdmin' )
	fields = ['titulo', 'dia', 'direccion' ,'f_inicio', 'f_finalizacion']

class EliminarEvento(LoginRequiredMixin,DeleteView):
	model = Evento
	template_name = 'Evento/eliminarEvento.html'
	success_url = reverse_lazy('evento:listarEventos')