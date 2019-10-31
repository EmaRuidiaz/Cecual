from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from apps.user.forms import RegistroForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


# Create your views here.

class RegistrarUsuario(CreateView):
	form_class = RegistroForm
	template_name = 'user/registro.html'
	success_url = reverse_lazy('start')   # + '?register'

	def get_form(self, form_class=None):
		form = super(RegistrarUsuario,self).get_form()
		form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de Usuario'})
		form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre'})
		form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Apellido'})
		form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección de Email'})
		form.fields['telefono'].widget = forms.TextInput(attrs={'class':'form-control mb-2',' placeholder':'Celular'})
		form.fields['direccion'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Direccion'})
		form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2',' placeholder':'Contraseña'})
		form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2',' placeholder':'Repite la contraseña'})
		return form
		