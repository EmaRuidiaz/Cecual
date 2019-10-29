from django.shortcuts import render
from apps.historia.models import Historia
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ListarHistoria(ListView):
	model = Historia
	template_name = 'Historia/listarHistoria.html'

class ModificarHistoria(LoginRequiredMixin,UpdateView):
	model = Historia
	template_name = 'Historia/modificarHistoria.html'
	success_url = reverse_lazy('historia:listarHistoria')
	fields = '__all__'

class AgregarHistoria(LoginRequiredMixin,CreateView):
	model = Historia
	template_name = 'Historia/modificarHistoria.html'
	success_url = reverse_lazy('historia:listarHistoria')
	fields = '__all__'