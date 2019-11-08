from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.producto.models import Producto
from apps.feriante.models import Feriante
from apps.categoria.models import Categoria
from apps.reserva.models import Reserva
from apps.pedido.models import Pedido
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from apps.producto.forms import ProductoForm
from apps.reserva.forms import ReservaForm
from apps.pedido.forms import PedidoForm
import collections
from decimal import Decimal
from django.contrib import messages
from django.http import Http404

class ListarProductos(ListView):
	model = Producto
	paginate_by = 12
	template_name = 'Producto/listar.html'
	form_class = PedidoForm

	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)
		print('anted de is_valid')
		pk = request.POST['Confirmar']
		print(pk)
		if form.is_valid():
			p = Producto.objects.get(pk = pk)
			res = form.save(commit = False)
			res.producto = p
			res.cliente = request.user
			cant = request.POST['cantidad']
			total = Decimal(cant) * p.precio
			print(total)
			res.total = total
            # Marca la casilla de envio
			# if request.POST['envio'] == 'Si':
			# 	res.envio = True
			# else:
			# 	res.envio = False
				
			res.save()
			print('Guardeeee')
			return HttpResponseRedirect('/producto/')
		return render(request,self.template_name, {'form':form})

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print (context)
		
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
		context['filtro'] = Categoria.objects.all()

		if self.request.user.is_authenticated:
			pedidos = Pedido.objects.filter(cliente = self.request.user)
			context['Pedido'] = pedidos

		return context

	def get_queryset(self):
		context = {}
		categoria = self.request.GET.get('Categoria',None)
		if not categoria:
			categoria = "0"
		
		if categoria == "0":
			x = Producto.objects.all()
		else:
			x = Producto.objects.filter(categoria = categoria)
		return x
	


class AgregarProductoo(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	#form = ProductoForm(request.POST or None, request.FILES)
	#form_class = ProductoForm
	model = Producto
	template_name = 'Producto/agregarProducto.html'
	fields = '__all__'
	success_url = reverse_lazy('producto:listar')
	success_message = 'Feriante agregado correctamente'

	'''
	
	REVISAR ESTE CODIGO CON NICO. NO ANDA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	'''

	#return render(request, 'Producto/agregarProducto.html', context)

def AgregarProducto(request): #Vistas basadas en funciones
	form = ProductoForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		ap = form.save(commit=False)
		ap.categoria = Categoria.objects.get(pk = request.POST.get('categoria'))
		ap.feriante = Feriante.objects.get(encargado = request.user.pk)
		ap.save()
		messages.success(request, 'Student added successfully') # este mensaje se tiene que modificar
		return redirect('producto:listar')


	return render(request, 'Producto/agregarProducto.html', {'form': form, 'categoria': Categoria.objects.all(), 'feriantes': Feriante.objects.all()})

class ModificarProducto(LoginRequiredMixin,UpdateView):
	model = Producto
	template_name = 'Producto/agregarProducto.html'
	fields = ['nombre', 'precio', 'stock', 'foto_producto', 'categoria', 'descripcion']
	success_url = reverse_lazy('producto:listar')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categoria'] = Categoria.objects.all()
	
		return context

class EliminarProducto(LoginRequiredMixin,DeleteView):
	model = Producto
	template_name = 'Producto/eliminarProducto.html'
	success_url = reverse_lazy('producto:listar')


class DetalleProducto(DetailView):
	model = Producto
	template_name = 'producto/detalle_producto.html'
	form_class = PedidoForm

	def get_context_data(self, **kwargs):
		context = super(DetalleProducto, self).get_context_data(**kwargs)
		categoria = Categoria.objects.filter(nombre = self.kwargs['categoria']).get()
		context_object_name = 'Sugerencia'
		list_sugerencia = Producto.objects.filter(categoria = categoria )
		
		cont = len(list_sugerencia)	
		iterador = 1
		cards=[]
		lista_productos=[]
		
		if cont > 3:
				
			for i in list_sugerencia:   
				cards.append(i) 
				if iterador % 3 == 0:
					lista_productos.append(cards) 
					#context['Sugerencia'] = cards
					print('esto es la lista de prod', lista_productos)
					cards=[]
					
					
				iterador += 1
					
			context['Sugerencia'] = lista_productos
			print('este es el contexto', context)
			return context
			
		else:
			
			return context
	
	def post(self,request,*args,**kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			p = Producto.objects.get(pk = self.kwargs['pk'])
			res = form.save(commit = False)
			res.producto = p
			res.cliente = request.user
			cant = request.POST['cantidad']
			total = Decimal(cant) * p.precio
			print(total)
			res.total = total
            # Marca la casilla de envio
			if request.POST['envio'] == 'Si':
				res.envio = True
			else:
				res.envio = False
				
			res.save()
			return HttpResponseRedirect('/producto/')
		return render(request,self.template_name, {'form':form})
