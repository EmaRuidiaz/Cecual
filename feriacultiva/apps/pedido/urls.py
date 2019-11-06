from django.contrib import admin
from django.urls import path
from . import views

app_name = "pedido"

urlpatterns = [

    #URL Principal
    path('', views.ListarPedido.as_view(), name="listarPedido"),

    #path('<int:pk>', views.ModificarHistoria.as_view(), name="modificarHistoria"),

    #path('agregarHistoria', views.AgregarHistoria.as_view(), name="agregarHistoria"),
]
