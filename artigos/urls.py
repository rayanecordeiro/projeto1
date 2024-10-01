from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ArtigosViewSet

router = DefaultRouter()
router.register(r'artigos', ArtigosViewSet)

urlpatterns = [
    path('', views.index, name='index'), 
    path('adicionar/', views.adicionar, name='adicionar'),  # Página para adicionar artigo
    path('excluir/<int:artigo_id>/', views.excluir, name='excluir'),  # Página para excluir artigo
    path('modificar/<int:artigo_id>/', views.modificar, name='modificar'),  # Página para modificar artigo
    path('', include(router.urls)),

]





