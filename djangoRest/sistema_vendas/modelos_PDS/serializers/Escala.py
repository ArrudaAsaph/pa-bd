from rest_framework import serializers
from modelos_PDS.models import Escala, Plantao

class EscalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escala
        fields = '__all__'