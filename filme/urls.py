# url - view - template

from django.urls import path, include
from .views import Homepage, Homefilmes, Detalhesfilme

app_name = 'filme' # nome do app para usar no template

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'), 
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme') # pk -> primary key (id do filme)
]