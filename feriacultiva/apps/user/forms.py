from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistroForm(UserCreationForm): 

    class Meta:
        model = User
        fields = ['username',
            'first_name',
            'last_name',
            'email',
            'password',
            'direccion', 
        ]
        # labels = {
        #     'username': 'Nombre de Usuario',
        #     'first_name': 'Nombre',
        #     'last_name': 'Apellido',
        #     'email': 'Correo electrionico',
        #     'password': 'Contraseña',
        #     'direccion': 'Direccion',
        # }