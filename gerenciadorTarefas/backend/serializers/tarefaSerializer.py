from rest_framework import serializers
from backend.models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    projeto = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Tarefa
        fields = [
            'id', 'titulo', 'descricao', 'projeto',
            'concluida', 'prioridade',
            'data_criacao', 'data_conclusao'
        ]
        read_only_fields = ['data_criacao', 'data_conclusao']
