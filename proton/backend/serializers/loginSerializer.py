from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    extra_kwargs = {'password': {'write_only': True}}
