from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Inicio(request):
	return render(request,'start.html')