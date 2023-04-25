from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class AuthView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data