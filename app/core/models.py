"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import UserManager, DepartmentManager


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self) -> str:
        return self.email


class Department(models.Model):
    """Department model"""
    dept_name = models.CharField(max_length=255)
    hod = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    objects = DepartmentManager()

    def natural_key(self):
        return (self.hod, self.dept_name)

    def __str__(self) -> str:
        return f'{self.dept_name}'
