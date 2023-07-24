"""
Helper functions
"""
from django.contrib.auth import get_user_model
from core import models


def create_user(**params):
    """Create a new user"""
    return get_user_model().objects.create_user(**params)


# department
def create_department(**params):
    return models.Department.objects.create(**params)
