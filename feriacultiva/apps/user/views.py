from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import User
from apps.user.forms import RegistroForm, EditarUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


# Create your views here.

class RegistrarUsuario(CreateView):
	form_class = RegistroForm
	template_name = 'user/registro.html'
	success_url = reverse_lazy('login')   # + '?register'
	
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
		form.fields['foto_perfil'].widget = forms.FileInput(attrs={'class':'form-control mb-2'})
		return form
		
def EditarPerfil(request):
	context = {}
	user = request.user
	usuario = User.objects.get(username = user)
	context['user'] = usuario
	print('antes del if')
	if request.method == 'GET':
		form = EditarUserForm(instance = usuario)
	else:
		form = EditarUserForm(request.POST, instance = usuario)
		if form.is_valid():
			perfil = form.save(commit = False)
			perfil.username = usuario.username
			if request.POST.get('foto_perfil') == '':
				perfil.foto_perfil = usuario.foto_perfil
			else:
				perfil.foto_perfil = request.POST.get('foto_perfil')
			perfil.first_name = request.POST.get('first_name')
			perfil.last_name = request.POST.get('last_name')
			perfil.email = usuario.email
			perfil.direccion = request.POST.get('direccion')
			perfil.save()
			
	return render(request,'user/perfil.html',context,{'form':form})
