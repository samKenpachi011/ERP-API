"""Employee api endpoints tests"""

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.helpers import create_user, create_department
from core.models import Employee
from personnel.serializers import EmployeeSerializer, EmployeeDetailsSerializer

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

    defaults.update(params)

    emp = Employee.objects.create(**defaults)
    return emp


def detail_url(emp_id):
    """Return the details url"""
    return reverse('personnel:employee-detail', args=[emp_id])


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

    def test_delete_employee(self):
        """Test detele employee"""

        emp = create_emp()
        url = detail_url(emp.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Employee.objects.filter(id=emp.id).exists())

    def test_partial_update(self):
        """Test partial update"""
        emp = create_emp()
        url = detail_url(emp.id)

        payload = {
            'first_name': 'Update'
        }

        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        emp.refresh_from_db()

        self.assertEqual(emp.first_name, payload['first_name'])

    def test_full_update(self):
        """Test full update"""

        dept = create_department(
            dept_name='Test department update',
            hod='Test update',
            description='Test description update'
        )

        defaults = {
            'first_name': 'Test Update',
            'last_name': 'Updated',
            'date_of_birth': '1991-01-01',
            'hired_date': '2020-01-01',
            'identity_type': 'country_id',
            'highest_qualification': 'diploma',
            'postal_address': 'P O Box 11100',
            'department': dept,
            'emp_code': 3212
        }

        self.emp = create_emp(**defaults)
        url = detail_url(self.emp.id)
        payload = {
            'first_name': 'Test Frank',
            'emp_code': 321
        }

        res = self.client.patch(url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.emp.refresh_from_db()

        for k, v in payload.items():
            if k == 'department':
                self.assertEqual(getattr(self.emp, k).id, v)
            else:
                self.assertEqual(getattr(self.emp, k), v)

    def test_get_employee_details(self):
        """Test get employee details"""
        emp = create_emp()
        url = detail_url(emp.id)

        res = self.client.get(url)

        serializer = EmployeeDetailsSerializer(emp)

        self.assertEqual(res.data, serializer.data)
