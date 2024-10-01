from rest_framework import serializers
from .models import Artigos

class ArtigosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigos
        fields = '__all__'
