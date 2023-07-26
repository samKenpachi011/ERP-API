"""Url mappings for the personnel app"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from personnel import views

app_name = 'personnel'

router = DefaultRouter()
router.register('department', views.DepartmentViewSet,
                basename='department')
router.register('employee', views.EmployeeViewSet,
                basename='employee')


urlpatterns = [
    path('', include(router.urls))
]
