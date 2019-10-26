from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
	phone_regex = RegexValidator(
		regex=r'\+?1?\d{9,15}$',
		message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed"
	)

	telefono = models.CharField(validators=[phone_regex], max_length=17, blank=True)

	es_empresa = models.BooleanField(default=False)

	foto_perfil = models.ImageField(upload_to = 'cliente', null = True)

	email = models.EmailField(
		'direccion de correo',
		unique=True,
		error_messages={
			'unique': 'Ya existe un usuario con este email.'
		}
	)

	direccion = models.CharField(max_length=200)

		