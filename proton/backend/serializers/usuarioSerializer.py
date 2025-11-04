from rest_framework import serializers
from backend.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 
            'username',
            'password',
            'email', 
            'first_name', 
            'last_name', 
            'bio', 
            'data_cadastro'
        ]
        extra_kwargs = {'password': {'write_only': True}}
