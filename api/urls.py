# api/urls.py

from django.urls import path, include  # Inclui o 'include' para rotear outras URLs
from rest_framework.routers import DefaultRouter  # Roteador do DRF
from artigos.views import ArtigosViewSet  # Importe o ArtigosViewSet da app 'artigos'

# Criar um roteador padrão
router = DefaultRouter()
router.register(r'artigos', ArtigosViewSet)  # Registra o endpoint 'artigos' no roteador

# Mapeia as rotas
urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas do roteador
]
