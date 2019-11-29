from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
	phone_regex = RegexValidator(
		regex=r'\+?1?\d{9,15}$',
		message=" El número de teléfono no es válido. ")
	
	first_name_regex = RegexValidator(
		regex=r'[a-zA-Z]',
		message=" El nombre no es válido. ")

	last_name_regex = RegexValidator(
		regex=r'[a-zA-Z]',
		message=" El apellido no es válido. ")

	first_name = models.CharField(validators=[first_name_regex], max_length=30)

	last_name = models.CharField(validators=[last_name_regex], max_length=150)

	telefono = models.CharField(validators=[phone_regex], max_length=17, blank=True)

	es_empresa = models.BooleanField(default=False)

	foto_perfil = models.ImageField(upload_to = 'cliente', null = True, default='cliente/user.png')

	email = models.EmailField(
		'direccion de correo',
		unique=True,
		error_messages={
			'unique': 'Ya existe un usuario con este email.'
		}
	)

	direccion = models.CharField(max_length=200)

		