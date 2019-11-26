from django.shortcuts import render
from django.views.generic.list import ListView
from apps.publicaciones.models import Publicacion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
class ListarPublicaciones(ListView):
	model = Publicacion
	template_name = 'Publicacion/listarPublicaciones.html'

class ListarPublicacionesAdmin(ListView):
	model = Publicacion
	template_name = 'Publicacion/listarPublicacionesAdmin.html'

class AgregarPublicacion(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Publicacion
	template_name = 'Publicacion/nuevaPublicacion.html'
	success_url = reverse_lazy('publicacion:listarPublicacionesAdmin')
	fields = '__all__'

class DetallePublicacion(DetailView):
	model = Publicacion
	template_name = 'Publicacion/detallePublicacion.html'

class ModificarPublicacion(LoginRequiredMixin,UpdateView):
	model = Publicacion
	template_name = 'Publicacion/agregarPublicacion.html'
	fields = ['foto','titulo', 'contenido' ]
	success_url = reverse_lazy('publicacion:listarPublicacionesAdmin' )
	

class EliminarPublicacion(LoginRequiredMixin,DeleteView):
	model = Publicacion
	template_name = 'Publicacion/listarPublicacionesAdmin.html'
	success_url = reverse_lazy('publicacion:listarPublicacionesAdmin')
