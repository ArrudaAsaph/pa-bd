from rest_framework import serializers
from backend.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'data_cadastro']
        read_only_fields = ['data_cadastro']
