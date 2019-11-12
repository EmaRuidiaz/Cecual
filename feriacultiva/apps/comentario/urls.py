from django.contrib import admin
from django.urls import path
from . import views

app_name = "comentario"

urlpatterns = [

    path('comentarios/<int:pk>', views.ListarComentario, name="Comentarios")

]