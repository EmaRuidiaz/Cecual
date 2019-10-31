from django.shortcuts import render
from apps.reserva.models import Reserva
from apps.producto.models import Producto
from apps.user.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
# Create your views here.

# def AgregarReserva(request,pk):
#     producto = Producto.objects.get(pk = pk)

class AgregarReserva(LoginRequiredMixin,CreateView):
    model = Reserva
    template_name = 'Reserva/reserva.html'
    fields = '__all__'

    def get_context_data(self, **kwargs): # pk, feriante
        context = super().get_context_data(**kwargs)
        producto = Producto.objects.get(pk = self.kwargs['pk'])
        user = User.objects.get(username = self.request.user)
        context['producto'] = producto
        context['usuario'] = user
        return context




    # hacer un form para registrar el producto con la cantidad de pedido.