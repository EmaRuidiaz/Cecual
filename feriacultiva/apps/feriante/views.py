from django.shortcuts import render
from apps.feriante.models import Feriante
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from apps.feriante.forms import FerianteForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class AgregarFeriante(SuccessMessageMixin, LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = Feriante
	form_class = FerianteForm
	template_name = 'Admin/agregarFeriante.html'
	success_url = reverse_lazy('feriante:agregar')
	success_message = 'Feriante agregado correctamente'