from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def Inicio(request):
	return render(request,'start.html')

@login_required
def  Administrador(request):
	return render(request, 'administrador.html')