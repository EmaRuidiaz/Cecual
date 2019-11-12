from django.shortcuts import render
from django.views.generic.list import ListView
from apps.tema.models import Tema
from apps.tema.forms import TemaForm
from django.core.paginator import Paginator

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
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        paginator = context['paginator']
        page_numbers_range = 10 #Cantidad de página que se va a mostrar 
        max_index = len(paginator.page_range)
        
        page = self.request.GET.get('page')
        print (self.request)
        current_page = int(page) if page else 1
        
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index
            
        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        
        return context