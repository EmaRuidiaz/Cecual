from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tema'

urlpatterns = [
    path('AgregarTema/', views.AgregarTema, name="Agregar"),

    path('ListaTema/', views.ListarTema.as_view(), name="ListarTema"),
]