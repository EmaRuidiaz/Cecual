from django.shortcuts import render, redirect
from apps.feriante.models import Feriante
from apps.producto.models import Producto
from apps.user.models import User
from apps.pedido.models import Pedido
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from apps.feriante.forms import FerianteForm, PerfilFerianteForm, PerfilUsuarioFeriante
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from apps.producto.models import Producto

from django.core.mail import send_mail



#vista para el template del administrador
class ListarFeriantes(ListView):
	model = Feriante
	template_name = 'Feriante/listarFeriantes.html'

#vista feriantes web
class ListarFeriantesWeb(ListView):
	model = Feriante
	paginate_by = 10
	template_name = 'Feriante/ListarFeriantesWeb.html'

	def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
			paginator = context['paginator']
			page_numbers_range = 10 #Cantidad de página que se va a mostrar 
			max_index = len(paginator.page_range)

			page = self.request.GET.get('page')
			print (self.request)
			current_page = int(page) if page else 1

			start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
			end_index = start_index + page_numbers_range
			if end_index >= max_index:
				end_index = max_index

			page_range = paginator.page_range[start_index:end_index]
			context['page_range'] = page_range
			print("Anónimo: ",self.request.user.username)
			try:
				pedidos = Pedido.objects.filter(cliente = self.request.user)
			except Exception as e:
				pedidos = []

			context['Pedido'] = pedidos

			return context

#Vistas basadas en clases
class AgregarFeriante(SuccessMessageMixin, LoginRequiredMixin,CreateView): 
	model = Feriante
	form_class = FerianteForm
	template_name = 'Admin/agregarFeriante.html'
	success_url = reverse_lazy('feriante:agregar')
	success_message = 'Feriante agregado correctamente'

@login_required
def EliminarFeriante(request,pk):
	print(pk)
	usuario = Feriante.objects.get(pk = pk).encargado
	print(usuario)
	usuario.is_active = False
	usuario.save()
	return redirect('feriante:listarFeriantes')


# Esto es lo nuevo.. debo seguir trabajando
def PerfilFeriante(request):
	encargado = request.user
	feria = Feriante.objects.get(encargado = encargado)
	p = User.objects.get(username = encargado)
	print(p)
	context = {}
	context['feria'] = feria
	context['usuario'] = p
	print('hola')

	if request.method == 'GET':
		form = PerfilFerianteForm(instance = feria)
		form2 = PerfilUsuarioFeriante(instance = p)
	else:
		form = PerfilFerianteForm(request.POST, instance = feria)
		form2 = PerfilUsuarioFeriante(request.POST, instance = p)
		if form.is_valid and form2.is_valid():
			perfil = form.save(commit = False)
			u = form2.save(commit = False)
			perfil.encargado = p
			if request.POST.get('foto_feriante') == '':
				perfil.foto_feriante = feria.foto_feriante
			else:
				perfil.foto_feriante = request.POST.get('foto_feriante')
			perfil.descripcion = request.POST.get('descripcion')
			if request.POST.get('delivery') == 'Si':
				perfil.delivery = True
			else:
				perfil.delivery = False

			u.first_name = request.POST.get('first_name')
			u.direccion = request.POST.get('direccion')
			u.telefono = request.POST.get('telefono')
			u.save()
			perfil.save()
			return redirect(reverse('feriante:detalle',kwargs={'pk':feria.pk}))
	return render(request,'Feriante/perfil.html',context,{'form':form,'form2':form2})
	


class DetalleFeriante(DetailView):
	model = Feriante
	template_name = 'Feriante/detalle_feriante.html'

	def MisProductos(self, request, pk):
		context = {}
		usuario = Feriante.objects.get(pk = self.kwargs['pk'])
		print("ESTA ES LA PK", usuario)
		productos = Producto.objects.filter(feriante = usuario )
		context['object_list'] = productos
		print( context)

		return context

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		p = Producto.objects.filter(feriante = self.kwargs['pk'])
		context['product'] = p
		return context


def MisProductos(request):
	context = {}
	feriante2 = Feriante.objects.get(encargado = request.user)
	print(feriante2)
	p = Producto.objects.filter(feriante = feriante2)
	context['product'] = p
	print(context)
	return render(request,'Feriante/MisProductos.html',context)


# Esta funcion envia un correo
def EnviarCorreo(request):
	send_mail('Prueba', # titulo
		'Esto es un correo de prueba', # mensaje
		'feriacultivasite@gmail.com', 
		['flechaverde_s88@hotmail.com','mauriypachi@hotmail.com'], # Para:
		fail_silently=False,
	)
	return render(request,'Producto/listar.html')