from django.contrib import admin
from django.urls import path
from . import views

app_name = "vote"

urlpatterns = [

    path('vote/<int:pk>', views.Votar, name="votar"),

]