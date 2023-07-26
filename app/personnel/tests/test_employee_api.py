"""Employee api endpoints tests"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.helpers import create_user, create_department
from core.models import Employee
from personnel.serializers import EmployeeSerializer

EMP_URL = reverse('personnel:employee-list')


def create_emp(**params):

    dept = create_department(
        dept_name='Test department',
        hod='Test Head of Department',
        description='Test department description'
    )

    defaults = {
        'first_name': 'Paul',
        'last_name': 'David',
        'date_of_birth': '1990-01-01',
        'hired_date': '2010-01-01',
        'identity_type': 'country_id',
        'highest_qualification': 'associates_degree',
        'postal_address': 'P O Box 11000',
        'department': dept,
        'emp_code': 123
    }

    defaults.update(**params)

    emp = Employee.objects.create(**defaults)
    return emp



class PublicEmployeeTest(TestCase):
    """Tests for unathenticated users"""
    def setUp(self) -> None:
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth required"""
        res = self.client.get(EMP_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateEmployeeTest(TestCase):
    """Tests for authenticated users"""

    def setUp(self) -> None:
        self.client = APIClient()

        self.user = create_user(
            email='testuser@example.com',
            password='testpassword'
        )

        self.client.force_authenticate(self.user)

    def test_retrieve_employees(self):
        """Test retrieve employees"""

        create_emp()
        create_emp()

        res = self.client.get(EMP_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.all().count(), 2)
        emps = Employee.objects.all().order_by('-id')
        serializer = EmployeeSerializer(emps, many=True)

        self.assertEqual(res.data, serializer.data)

    def test_create_employee(self):
        """Test create employee"""

        dept = create_department(
            dept_name='Test department',
            hod='Test Head of Department',
            description='Test department description'
        )

        payload = {
            'first_name': 'Pearl',
            'last_name': 'David',
            'date_of_birth': '1990-01-01',
            'hired_date': '2010-01-01',
            'identity_type': 'country_id',
            'highest_qualification': 'associates_degree',
            'postal_address': 'P O Box 11000',
            'department': dept.id,
            'emp_code': 123
        }

        res = self.client.post(EMP_URL, payload, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        emp = Employee.objects.get(id=res.data['id'])
        self.assertEqual(payload['first_name'], emp.first_name)
