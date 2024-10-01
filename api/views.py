from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Artigos
from .serializers import ArtigosSerializer

class ArtigosViewSet(viewsets.ModelViewSet):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
