from django.contrib import admin
from django.urls import path
from . import views

app_name = "feriante"

urlpatterns = [

    #URL Principal
    path('agregarFeriante/', views.AgregarFeriante.as_view(), name="agregar"),

    path('', views.ListarFeriantes.as_view(), name="listarFeriantes"),

]
