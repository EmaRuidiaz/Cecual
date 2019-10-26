from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Inicio(request):
	if request.user.username == 'admin':
		return render(request, 'administrador.html')	
	else:
		return render(request,'start.html')

def  Administrador(request):
	return render(request, 'administrador.html')