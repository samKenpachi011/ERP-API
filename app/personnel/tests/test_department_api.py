"""Test department api endpoints"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.helpers import create_user, create_department
from core.models import Department
from personnel.serializers import (
    DepartmentSerializer,
    DepartmentDetailsSerializer)


DEPT_URL = reverse('personnel:department-list')


def details_url(department_id):
    """Return department details url"""
    return reverse('personnel:department-detail', args=[department_id])


class PublicDepartmentTests(TestCase):
    """Tests for unautheticated users"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth required"""

        res = self.client.get(DEPT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateDepartmentTests(TestCase):
    """Tests for authenticated users"""

    def setUp(self):
        self.client = APIClient()

        self.user = create_user(
            email='testuser@example.com',
            password='testpassword'
        )

        self.client.force_authenticate(self.user)

    def test_retrieve_departments(self):
        """Test list departments"""

        default1 = {
            'dept_name': 'Test Dept 1',
            'hod': 'Test HOD 1',
            'description': 'Department description 1',
        }

        default2 = {
            'dept_name': 'Test Dept 2',
            'hod': 'Test HOD 2',
            'description': 'Department description 2',
        }

        create_department(**default1)
        create_department(**default2)

        res = self.client.get(DEPT_URL)

        depts = Department.objects.all().order_by('-id')

        serializer = DepartmentSerializer(depts, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_department(self):
        """Test creating department"""
        payload = {
            'dept_name': 'Test Dept 3',
            'hod': 'Test HOD 3',
            'description': 'Department description 3',
        }

        res = self.client.post(DEPT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        dept = Department.objects.get(id=res.data['id'])
        self.assertEqual(payload['dept_name'], dept.dept_name)

    def test_delete_department(self):
        """Test delete department"""
        default4 = {
            'dept_name': 'Test Dept 4',
            'hod': 'Test HOD 4',
            'description': 'Department description 4',
        }
        dept = create_department(**default4)
        url = details_url(dept.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Department.objects.filter(id=dept.id).exists())

    def test_dept_partial_update(self):
        """Test partial department update"""
        default5 = {
            'dept_name': 'Test Dept 5',
            'hod': 'Test HOD 5',
            'description': 'Department description 5',
        }
        dept = create_department(**default5)
        payload = {
            'hod': 'Test HOD Update',
        }

        url = details_url(dept.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        dept.refresh_from_db()
        self.assertEqual(payload['hod'], dept.hod)

    def test_dept_full_update(self):
        """Test full department update"""
        default6 = {
            'dept_name': 'Test Dept 6',
            'hod': 'Test HOD 6',
            'description': 'Department description 6',
        }
        dept = create_department(**default6)

        url = details_url(dept.id)

        payload = {
            'dept_name': 'Test Dept Update',
            'hod': 'Test HOD Update',
            'description': 'Department description update',
        }

        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        dept.refresh_from_db()

        for k, v in payload.items():
            self.assertEqual(getattr(dept, k), v)

    def test_get_department_detials(self):
        """Test get department details"""
        default7 = {
            'dept_name': 'Test Dept 7',
            'hod': 'Test HOD 7',
            'description': 'Department description 7',
        }
        dept = create_department(**default7)

        url = details_url(dept.id)

        res = self.client.get(url)

        serializer = DepartmentDetailsSerializer(dept)

        self.assertEqual(res.data, serializer.data)
