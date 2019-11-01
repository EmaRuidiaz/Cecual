from django.shortcuts import render, redirect
from apps.feriante.models import Feriante
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from apps.feriante.forms import FerianteForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView

class ListarFeriantes(ListView):
	model = Feriante
	template_name = 'Feriante/listarFeriantes.html'


class AgregarFeriante(SuccessMessageMixin, LoginRequiredMixin,CreateView): #Vistas basadas en clases
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

