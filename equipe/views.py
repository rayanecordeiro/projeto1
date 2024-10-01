from django.shortcuts import render
from . models import Equipe 
from . forms import EquipeForm

# Create your views here.
def index(request):
    #Consulta da equipe
    equipe = Equipe.objects.all()
    context = {
        'lista': equipe 
    }
    return render(request, 'equipe.html', context)

def adicionar(request):
    form = EquipeForm()
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = EquipeForm()
            return render(request, 'adicionar_equipe.html', {'form': form})
        else:
            form = EquipeForm() 

    return render(request, 'adicionar_equipe.html', {'form': form})

    
