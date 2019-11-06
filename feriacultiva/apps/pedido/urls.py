from django.contrib import admin
from django.urls import path
from . import views

app_name = "pedido"

urlpatterns = [

    #URL Principal
    path('', views.ListarPedido, name="listarPedido"),

    path('delete/<int:pk>', views.DeletePedido, name="delete"),

    #path('agregarHistoria', views.AgregarHistoria.as_view(), name="agregarHistoria"),
]
