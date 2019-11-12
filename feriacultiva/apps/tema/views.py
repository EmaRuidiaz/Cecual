from django.shortcuts import render
from django.views.generic.list import ListView
from apps.tema.models import Tema
from apps.tema.forms import TemaForm

# Create your views here.

def AgregarTema(request):
    user = request.user
    if request.method == 'GET':
        form = TemaForm(request.POST)
    else:
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save(commit = False)
            tema.creador = user
            tema.comentario = request.POST.get('comentario')
            tema.titulo = request.POST.get('titulo')
            tema.save()
    
    return render(request,'Foro/crear_tema.html',{'form':form})

class ListarTema(ListView):
    model = Tema
    template_name = 'Foro/listar_foro.html'