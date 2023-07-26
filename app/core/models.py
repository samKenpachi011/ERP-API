"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import UserManager, DepartmentManager
from .choices import IDENTITY_TYPES, HIGHEST_QUALIFICATIONS


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
        return self.dept_name


class Employee(models.Model):
    """Employee model"""
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    hired_date = models.DateField(null=True, blank=True)
    identity_type = models.CharField(choices=IDENTITY_TYPES,
                                     max_length=50, blank=True)
    highest_qualification = models.CharField(choices=HIGHEST_QUALIFICATIONS,
                                             max_length=50, blank=True)
    postal_address = models.CharField(max_length=200, blank=True)
    department = models.ForeignKey('Department',
                                   on_delete=models.SET_NULL,
                                   null=True, blank=True)
    emp_code = models.PositiveIntegerField(default=1, blank=True,
                                           null=True)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name} {self.emp_code}'
