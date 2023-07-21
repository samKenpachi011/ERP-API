"""Tests for models"""
from django.test import TestCase
from core.helpers import create_user, get_user_model


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
