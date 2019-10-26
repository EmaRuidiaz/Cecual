from django.contrib import admin
from django.urls import path
from . import views

app_name = "historia"

urlpatterns = [

    #URL Principal
    path('', views.ListarHistoria.as_view(), name="listarHistoria"),

    path('<int:pk>', views.ModificarHistoria.as_view(), name="modificarHistoria"),

    path('agregarHistoria', views.AgregarHistoria.as_view(), name="agregarHistoria"),
]
