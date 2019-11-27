from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [

    #URL Principal
    path('', views.RegistrarUsuario.as_view(), name="agregar"),

    path('editarperfil', views.EditarPerfil, name="editarperfil"),

    path('perfil', views.Perfil, name="perfil"),

]