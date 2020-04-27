from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from apps.publicaciones.models import Publicacion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from apps.pedido.models import Pedido
from django.db.models import Sum
from apps.publicaciones.forms import PublicacionForm, VideoForm
from apps.video.models import Video

# Create your views here.
class ListarPublicaciones(ListView):
	model = Publicacion
	template_name = 'Publicacion/listarPublicaciones.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.request.user.is_authenticated:
			pedidos = Pedido.objects.filter(cliente = self.request.user).aggregate(Sum('cantidad'))
			context['Pedido'] = pedidos

		return context

class ListarPublicacionesAdmin(ListView):
	model = Publicacion
	template_name = 'Publicacion/listarPublicacionesAdmin.html'

class AgregarPublicacion(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Publicacion
	template_name = 'Publicacion/nuevaPublicacion.html'
	success_url = reverse_lazy('publicacion:listarPublicacionesAdmin')
	fields = '__all__'


# -- Muestra la Publicacion seleccionada con sus videos e informacion en el contenido
# context[vid]: Son los videos que estan relacionados a la publicacion que se ha seleccionado.
def DetallePublicacion(request,pk):
	context={}
	p = Publicacion.objects.get(pk = pk)
	context['object'] = p
	v = Video.objects.filter(publicacion = p) #-Trae todos los videos de la publicacion, cambiar por el de arriba
	context['vid'] = v

	return render(request,'Publicacion/detallePublicacion.html',context)
	

# Modifiac una publicacion seleccionada y te permite agregar videos, por el momento no se puede modificar la foto
def ModificarPublicacion(request,pk):
	context = {}
	public = Publicacion.objects.get(pk = pk)
	context['public'] = public
	context['vid'] = Video.objects.filter(publicacion = pk)
	
	print('editar publicacion')
	if request.method == 'GET':
		form1 = PublicacionForm(instance = public)
		form2 = VideoForm #Link de los videos
	else:
		form1 = PublicacionForm(request.POST or None, request.FILES or None, instance=public)
		form2 = VideoForm(request.POST or None, request.FILES or None)
		
		# print(form1.is_valid()) #Son para comprobar si entra en los formularios
		# print(form2.is_valid())
		if form1.is_valid() and form2.is_valid():
			a = form2.save(commit=False)
			p = form1.save(commit=False)
			p.titulo = request.POST.get('titulo')
			if request.POST.get('foto') == '':
				p.foto = public.foto
			else:
				p.foto = request.FILES.get('foto')
				
			p.contenido = request.POST.get('contenido')
			if request.POST.get('lik_video') != '':
				a.link_video = request.POST.get('link_video')
				a.publicacion = public
			p.save()
			a.save()
			# Guarda toda la información modificada en ambos formularios		
		
	return render (request,'Publicacion/editarPublicacion.html',context,{form1:'form1', form2:'form2'})


# Entra con la clave del video, busca a que publicacion pertenece para mandar luego la id y elimina fisicamente el video
def EliminarVideo(request,pk):

	context={}
	v = Video.objects.get(pk = pk)
	pub = Publicacion.objects.get(titulo = v.publicacion.titulo)
	context['public'] = pub
	context['vid'] = Video.objects.filter(publicacion = pub.pk)
	Video.objects.get(pk = pk).delete() # Elimina el video
	
	return redirect('publicacion:modificarPublicacion', pk = pub.pk) #Redirecciono a la funcion ModificarPublicacion pasando la id de la publicacion
	

class EliminarPublicacion(LoginRequiredMixin,DeleteView):
	model = Publicacion
	template_name = 'Publicacion/listarPublicacionesAdmin.html'
	success_url = reverse_lazy('publicacion:listarPublicacionesAdmin')
