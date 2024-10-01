from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect 
from . models import Artigos 
from . forms import ArtigosSearchForm, ArtigosForm
from rest_framework import viewsets
from .serializers import ArtigosSerializer
    
def index(request):
    # Captura parâmetros de busca do formulário
    search_query = request.GET.get('search', '')
    autor = request.GET.get('autor', '')
    revista = request.GET.get('revista', '')
    palavras_chave = request.GET.get('palavras_chave', '')
    ano = request.GET.get('ano', '')
    resumo = request.GET.get('resumo', '')

    # Criação do filtro dinâmico
    artigos = Artigos.objects.all()

    if search_query:
        artigos = artigos.filter(titulo__icontains=search_query)
    if autor:
        artigos = artigos.filter(autores__icontains=autor)
    if revista:
        artigos = artigos.filter(revista__icontains=revista)
    if palavras_chave:
        artigos = artigos.filter(palavras_chave__icontains=palavras_chave)
    if ano:
        artigos = artigos.filter(ano=ano)
    if resumo:
        artigos = artigos.filter(resumo__icontains=resumo)

    # Ordenação por ano, o mais recente primeiro
    artigos = artigos.order_by('-ano')

    # Paginação (10 artigos por página)
    paginator = Paginator(artigos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_form': ArtigosSearchForm()
    }
    return render(request, 'artigos.html', context)


# Função para adicionar artigos
def adicionar(request):
    if request.method == "POST":
        form = ArtigosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Agora o método save vai funcionar
            return redirect('index')  # Redireciona para a página de visualização dos artigos
    else:
        form = ArtigosForm()

    context = {
        'form': form
    }
    return render(request, 'adicionar_artigos.html', context)

# Função para excluir artigos
def excluir(request, artigo_id):
    artigo = get_object_or_404(Artigos, id=artigo_id)
    
    if request.method == "POST":
        artigo.delete()
        return redirect('index')  # Redireciona para a página de visualização dos artigos
    
    context = {
        'artigo': artigo
    }
    return render(request, 'confirmar_exclusao.html', context)

# Função para modificar artigos
def modificar(request, artigo_id):
    artigo = get_object_or_404(Artigos, id=artigo_id)  # Busca o artigo pelo ID
    
    if request.method == "POST":
        form = ArtigosForm(request.POST, request.FILES, instance=artigo)  # Preenche o formulário com os dados atuais
        if form.is_valid():
            form.save()  # Salva as modificações no banco de dados
            return redirect('index')  
    else:
        form = ArtigosForm(instance=artigo)  # Preenche o formulário com os dados existentes do artigo

    context = {
        'form': form,
        'artigo': artigo
    }
    return render(request, 'modificar_artigos.html', context)



class ArtigosViewSet(viewsets.ModelViewSet):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

