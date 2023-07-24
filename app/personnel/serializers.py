"""
Serializer for Personnel Api's
"""
from rest_framework import serializers
from core.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for the department mdoel"""

    class Meta:
        model = Department
        fields = ['id', 'dept_name']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a new department override"""

        dept = Department.objects.create(**validated_data)
        return dept

    def update(self, instance, validated_data):
        """Update a department override"""

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class DepartmentDetailsSerializer(DepartmentSerializer):
    """Serializer for department details view"""
    class Meta(DepartmentSerializer.Meta):
        fields = DepartmentSerializer.Meta.fields + ['hod', 'description']
