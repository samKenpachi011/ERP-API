"""
Views for the user api
"""
from rest_framework import generics
from user.serializer import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a user"""

    serializer_class = UserSerializer
