from rest_framework import serializers
from backend.models import Projeto

class ProjetoSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Projeto
        fields = [
            'id', 'nome', 'descricao', 'usuario',
            'data_criacao', 'data_atualizacao', 'status'
        ]
        read_only_fields = ['usuario', 'data_criacao', 'data_atualizacao']
