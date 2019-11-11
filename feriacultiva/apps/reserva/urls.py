from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reserva'

urlpatterns = [
    path('reserva/', views.AgregarReserva, name = 'agregar'),

    path('reservas/', views.ListarReservasCliente, name = 'listar'),

    path('solicitudes/', views.ListarReservasFeriante, name = 'listarParaFeriante'),

    path('confirmar/<int:pk>', views.ConfirmarReserva, name = 'confirmar')
]