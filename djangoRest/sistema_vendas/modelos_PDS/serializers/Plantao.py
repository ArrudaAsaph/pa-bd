from rest_framework import serializers
from modelos_PDS.models import  Plantao

class PlantaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantao
        fields = '__all__'
