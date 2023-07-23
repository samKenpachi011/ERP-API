"""
Helper functions
"""
from django.contrib.auth import get_user_model


def create_user(**params):
    """Create a new user"""
    return get_user_model().objects.create_user(**params)
