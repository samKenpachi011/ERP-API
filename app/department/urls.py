"""Url mappings for the department app"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from department import views

app_name = 'department'

router = DefaultRouter()

router.register('department', views.DepartmentViewSet,
                basename=app_name)


urlpatterns = [
    path('', include(router.urls))
]
