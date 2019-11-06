from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.reserva.models import Reserva
from apps.pedido.models import Pedido
# Create your views here.


def AgregarReserva(request): 

	
	b = Reserva.objects.all()
	if len(b) == 0:
		n_ped = 1
	else:
		n_ped = Reserva.objects.order_by('n_pedido').last().n_pedido + 1

	print(n_ped)

	pedidos = Pedido.objects.filter(cliente = request.user)

	for pedido in pedidos:
		print(pedido.producto.nombre)
		Reserva.objects.create(n_pedido = n_ped, producto = pedido.producto, cantidad = pedido.cantidad, precio = pedido.total, user = pedido.cliente, envio = pedido.envio)
	
	
	Pedido.objects.filter(cliente = request.user).delete()
	'''	
	if form.is_valid():
		ap = form.save(commit=False)
		ap.categoria = Categoria.objects.get(pk = request.POST.get('categoria'))
		ap.feriante = Feriante.objects.get(encargado = request.user.pk)
		ap.save()
		messages.success(request, 'Student added successfully')
		return redirect('producto:listar')

'''
	return render(request, 'Pedido/listarPedidos.html', {'object_list': Pedido.objects.filter(cliente = request.user)})