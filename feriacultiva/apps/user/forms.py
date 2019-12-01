from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistroForm(UserCreationForm): 

    email = forms.EmailField(required = True)
    telefono = forms.CharField(max_length=17)
    direccion = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','direccion','password1','password2','foto_perfil')

class EditarUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','direccion','foto_perfil','telefono','email']
        