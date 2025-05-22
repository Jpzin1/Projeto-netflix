from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8] # "-" define que está em ordem decrescente
    return {"lista_filmes_recentes": lista_filmes}

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:8]
    return {"lista_filmes_em_alta": lista_filmes}

