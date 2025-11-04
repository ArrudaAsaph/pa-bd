rom rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token

from backend.models import Usuario
from backend.serializers import UsuarioSerializer

class AuthView(viewset.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


    @api_view(['POST'])
    def login(resquest):
        user = get_object_or_404(Usuario, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'message': 'Not Found!'}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        serializer = MeuUsuarioSerializer(instance=user)
        return Response({'token': token.key, 'user':serializer.data})