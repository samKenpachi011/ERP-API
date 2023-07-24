""""
View for personnel information
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from personnel import serializers
from core.models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    """View for managing department information"""
    serializer_class = serializers.DepartmentDetailsSerializer
    queryset = Department.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        """Return a serializer class for the request"""
        if self.action == 'list':
            return serializers.DepartmentSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new department"""
        return serializer.save()
