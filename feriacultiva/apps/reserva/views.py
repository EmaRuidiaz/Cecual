from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from apps.reserva.models import Reserva
from apps.pedido.models import Pedido
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from apps.feriante.models import Feriante
# Create your views here.

@login_required
def AgregarReserva(request): 

	
	b = Reserva.objects.all()
	if len(b) == 0:
		n_ped = 1
	else:
		n_ped = Reserva.objects.order_by('n_pedido').last().n_pedido + 1

	print(n_ped)

	pedidos = Pedido.objects.filter(cliente = request.user)
	user = request.user

	for pedido in pedidos:
		print(pedido.producto.nombre)

		email = pedido.producto.feriante.encargado.email
		producto = pedido.producto.nombre
		foto_producto = pedido.producto.foto_producto
		cantidad = pedido.cantidad

		
		Reserva.objects.create(n_pedido = n_ped, direccion_de_envio = pedido.cliente.direccion ,feriante = pedido.producto.feriante, producto = pedido.producto, cantidad = pedido.cantidad, precio = pedido.total, user = pedido.cliente, envio = pedido.envio)
		html_content = render_to_string('Feriante/email.html',{'email': email,
			'user_name': user,
			'producto_name': producto,
			'foto_producto': foto_producto,
			'cantidad': cantidad})

		send_mail('Reserva',
			producto,
			'feriacultivasite@gmail.com',
			[email],
			fail_silently = False,
			html_message = html_content,
		)
	

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
	return render(request, 'Reserva/listarReservas.html', {'object_list': Reserva.objects.filter(user = request.user)})

@login_required
def ListarReservasCliente(request):

	return render(request, 'Reserva/listarReservas.html', {'object_list': Reserva.objects.filter(user = request.user)})

@login_required
def ListarReservasFeriante(request):

	return render(request, 'Reserva/listarReservasParaFeriante.html', {'object_list': Reserva.objects.filter(feriante = Feriante.objects.get(encargado = request.user))})

def ConfirmarReserva(request, pk):

	Reserva.objects.filter(pk = pk).update(estado = True)

	return render(request, 'Reserva/listarReservasParaFeriante.html', {'object_list': Reserva.objects.filter(feriante = Feriante.objects.get(encargado = request.user))})
