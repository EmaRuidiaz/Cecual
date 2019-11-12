from django.shortcuts import render
from apps.tema.models import Tema
from apps.comentario.models import Comentario
from apps.comentario.forms import ComentarioForm

# Create your views here.

def ListarComentario(request,pk):
    context = {}
    print(pk)
    p = Tema.objects.get(pk = pk)
    print(p)
    x = Comentario.objects.filter(foro = p)
    print(x)
    context['comentario'] = x
    print(context)

    user = request.user
    if request.method == 'GET':
        form = ComentarioForm(request.POST)
    else:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            com = form.save(commit = False)
            com.user = user
            com.foro = p
            com.comentario = request.POST.get('comentario')
            com.save()
    
    return render(request,'Foro/comentario.html',context,{'form':form})