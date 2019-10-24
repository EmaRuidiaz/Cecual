from django.contrib import admin
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [

    #URL Principal
    path('', views.AgregarUser.as_view(), name="agregar"),

]