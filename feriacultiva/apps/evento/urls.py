from django.contrib import admin
from django.urls import path
from . import views

app_name = "evento"

urlpatterns = [

    path('', views.ListarEventos.as_view(), name="listarEventos"),

    path('agregarevento', views.AgregarEvento.as_view(), name="agregarEvento"),

    path('detalleevento/<int:pk>', views.DetalleEvento.as_view(), name="detalleEvento"),

    path('modificarevento/<int:pk>', views.ModificarEvento.as_view(), name="modificarEvento"),

    path('eliminarevento/<int:pk>', views.EliminarEvento.as_view(), name="eliminarEvento"),
]
