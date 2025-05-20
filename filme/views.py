from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class Homepage(TemplateView):
    template_name = 'homepage.html'

class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # object_list -> lista de itens do modelo

class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # contabilizar uma visualização
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # Filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme dapágina (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    