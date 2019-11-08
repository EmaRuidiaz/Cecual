from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reserva'

urlpatterns = [
    path('reserva/', views.AgregarReserva, name = 'agregar'),

    path('reservas/', views.ListarReservas, name = 'listar'),
]