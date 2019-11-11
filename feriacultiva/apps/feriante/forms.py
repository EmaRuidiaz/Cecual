from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from apps.user.models import User
from django.contrib.auth.models import Group
from .models import Feriante

class FerianteForm(UserCreationForm):

	#descripcion = forms.CharField(label=("Descripción"), required=True)
	#foto_feriante = forms.ImageField(required=False)
	#delivery = forms.BooleanField(required=False)

	'''
	descripcion = models.TextField()
	foto_feriante = models.ImageField(upload_to = 'feriante', null = True)
	delivery = models.BooleanField(default=False)
	encargado = models.OneToOneField(User, on_delete=models.CASCADE)
	'''

	class Meta:
		model = User
		#fields = ['username','first_name','last_name','password','foto_perfil','email','direccion']
		fields = ['username','first_name','last_name','password1','password2','telefono','email']

	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.es_empresa = True
		user.username = self.cleaned_data.get('username')
		user.is_staff = True
		p = Group.objects.get(name = 'feriante')
		user.save()
		p.user_set.add(user)
		empresa = Feriante.objects.create(descripcion = 'vacio',encargado = user)
		return user



class PerfilFerianteForm(forms.ModelForm):

	class Meta:
		model = Feriante
		fields = ['foto_feriante','descripcion','delivery']

class PerfilUsuarioFeriante(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name','direccion','telefono']