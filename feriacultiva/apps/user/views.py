from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from apps.user.forms import RegistroForm


# Create your views here.

class AgregarUser(LoginRequiredMixin,CreateView): #Vistas basadas en clases
	model = User
	template_name = 'User/agregarUser.html'
	fields = ['username','first_name','last_name','password','es_empresa','foto_perfil','email','direccion']
	success_url = reverse_lazy('feriante:agregar')

