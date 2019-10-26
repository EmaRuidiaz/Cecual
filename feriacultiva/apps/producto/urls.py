from django.contrib import admin
from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('producto/', views.ListarProductos.as_view(), name = "ListarProducto"),
    path('Detalle/<int:pk>', views.DetalleProducto.as_view(), name='Detalle'),
    path('agregar/', views.AgregarProducto.as_view(), name="agregar"),
    path('', views.ListarProductos.as_view(), name="listar"),
    path('detalle/<int:pk>', views.DetalleProducto.as_view(), name="detalle"),
    path('modificar/<int:pk>', views.ModificarProducto.as_view(), name="modificar"),
    path('eliminar/<int:pk>', views.EliminarProducto.as_view(), name="eliminar"),
]