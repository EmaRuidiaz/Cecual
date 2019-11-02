from django.shortcuts import render, redirect
from apps.feriante.models import Feriante
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from apps.feriante.forms import FerianteForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.core.paginator import Paginator


#vista para el template del administrador
class ListarFeriantes(ListView):
	model = Feriante
	template_name = 'Feriante/listarFeriantes.html'

#vista feriantes web
class ListarFeriantesWeb(ListView):
	model = Feriante
	paginate_by = 9
	template_name = 'Feriante/ListarFeriantesWeb.html'

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

