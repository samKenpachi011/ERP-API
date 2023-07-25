"""Tests for models"""
from django.test import TestCase
from core.helpers import create_user, get_user_model
from core import models
from core.helpers import create_department


class ModelTests(TestCase):
    """Tests for models"""

    def test_create_user_success(self):
        """Test creating a user"""

        email = 'test@example.com'
        password = 'testpassword'

        user = create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'pass123')
            self.assertEqual(user.email, expected)

    def test_user_without_email_raise_error(self):
        """Test email is not empty"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'pass123')

    def test_creating_superuser(self):
        """Test to create a super user"""
        user = get_user_model().objects.create_superuser(
            'admin@example.com', 'testadminpass123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

# Department model test
    def test_create_department(self):
        """Test creating a department success"""

        department = models.Department.objects.create(
            dept_name='Test department',
            hod='Test Head of Department',
            description='Test department description'
        )

        self.assertEqual(str(department), department.dept_name)

# Employee model test
    def test_create_employee(self):
        """Test creating an employee success"""

        self.dept = create_department(
            dept_name='Test department',
            hod='Test Head of Department',
            description='Test department description'
        )

        employee = models.Employee.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth='1990-01-01',
            hired_date='2010-01-01',
            identity_type='country_id',
            highest_qualification='associates_degree',
            postal_address='P O Box 10000',
            department=self.dept,
            emp_code=123
        )

        self.assertEqual(
            str(employee),
            f'{employee.first_name}, {employee.last_name} {employee.emp_code}')
