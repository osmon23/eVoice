from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainPairSerializer

Worker = get_user_model()

class WorkerLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)