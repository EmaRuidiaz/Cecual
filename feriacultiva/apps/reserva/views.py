from django.shortcuts import render
from apps.reserva.models import Reserva
from apps.producto.models import Producto
from apps.user.models import User
from apps.reserva.forms import ReservaForm
from django import forms
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
# Create your views here.

class AgregarReserva(DetailView):
    model = Producto
    template_name = 'Reserva/reserva.html'
    form_class = ReservaForm
    
    def get_context_data(self,**kwargs):
        context = super(AgregarReserva, self).get_context_data(**kwargs)
        p = Producto.objects.get(pk = self.kwargs['pk'])
        context['object'] = p
        return context

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            p = Producto.objects.get(pk = self.kwargs['pk'])
            res = form.save(commit = False)
            res.producto = p
            res.user = request.user
            # Marca la casilla de envio
            if request.POST['envio'] == 'Si':
                res.envio = True
            else:
                res.envio = False

            res.save()
            return HttpResponseRedirect('/producto/')
        return render(request,self.template_name, {'form':form})