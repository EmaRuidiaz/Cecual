from django.shortcuts import render
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Producto
from apps.categoria.models import Categoria
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

class ListarProductos(ListView):
    model = Producto
    paginate_by = 12
    template_name = 'Producto/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print (context)
        print('context')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro'] = Categoria.objects.all()
    
        return context

class AgregarProducto(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Producto
	template_name = 'Producto/agregarProducto.html'
	success_url = reverse_lazy('producto:listar')
	fields = '__all__'

class ModificarProducto(LoginRequiredMixin,UpdateView):
	model = Producto
	template_name = 'Producto/agregarProducto.html'
	success_url = reverse_lazy('productos:listar')
	fields = '__all__'

class EliminarProducto(LoginRequiredMixin,DeleteView):
	model = Producto
	template_name = 'Producto/eliminarProducto.html'
	success_url = reverse_lazy('productos:listar')

class DetalleProducto(DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'

    def get_context_data(self, **kwargs):
        context = super(DetalleProducto, self).get_context_data(**kwargs)
        categoria = Categoria.objects.filter(nombre = self.kwargs['categoria']).get()
        context_object_name = 'Sugerencia'
        list_sugerencia = Producto.objects.filter(categoria = categoria )
        context['Sugerencia'] = list_sugerencia
        return context
