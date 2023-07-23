"""
Views for the user api
"""
from rest_framework import generics
from user.serializer import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Create a user"""

    serializer_class = UserSerializer


class CreateAuthTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
