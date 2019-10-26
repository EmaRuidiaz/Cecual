from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from apps.user.forms import RegistroForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class AgregarUser(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = User
	template_name = 'user/registro.html'
	fields = ['username','first_name','last_name','password','es_empresa','foto_perfil','email','direccion']
	success_url = reverse_lazy('start')

