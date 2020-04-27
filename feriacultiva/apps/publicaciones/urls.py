from django.contrib import admin
from django.urls import path
from . import views

app_name = "publicacion"

urlpatterns = [

    path('', views.ListarPublicaciones.as_view(), name="listarPublicaciones"),

    path('GestionPublicaciones', views.ListarPublicacionesAdmin.as_view(), name="listarPublicacionesAdmin"),

    path('agregarpublicacion', views.AgregarPublicacion.as_view(), name="agregarPublicacion"),

    path('detallepublicacion/<int:pk>', views.DetallePublicacion, name="detallePublicacion"),

    path('modificarpublicacion/<int:pk>', views.ModificarPublicacion, name="modificarPublicacion"),

    path('eliminarpublicacion/<int:pk>', views.EliminarPublicacion.as_view(), name="eliminarPublicacion"),

    path('eliminarvideo/<int:pk>', views.EliminarVideo, name="eliminarVideo"),
]
