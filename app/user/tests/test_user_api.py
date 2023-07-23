"""
Tests for the user API.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from core.helpers import create_user

CREATE_USER_API = reverse('user:create')


class PublicUserApiTests(TestCase):
    """Public user API tests"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_pass(self):
        """Test creating a user"""

        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }

        res = self.client.post(CREATE_USER_API, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # check user credentials
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists_error(self):
        """Test user exists"""

        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }

        create_user(**payload)

        res = self.client.post(CREATE_USER_API, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test user exists"""

        payload = {
            'email': 'testuser@example.com',
            'password': 't23',
            'name': 'Test Name',
        }

        res = self.client.post(CREATE_USER_API, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']).exists()

        self.assertFalse(user_exists)
