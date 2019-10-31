from django.contrib import admin
from django.urls import path
from . import views

app_name = 'reserva'

urlpatterns = [
    path('reserva/<int:pk>', views.AgregarReserva.as_view(), name = 'Addreserva'),
]