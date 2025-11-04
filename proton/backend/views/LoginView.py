from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from backend.serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):

        login_serializer = LoginSerializer(request.data)
        
