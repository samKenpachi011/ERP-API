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
TOKEN_URL = reverse('user:token')
PROFILE_URL = reverse('user:profile')


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

    def test_create_token(self):
        """Test create token"""

        payload = {
            'email': 'testuser@example.com',
            'password': 'password123',
            'name': 'Test Name',
        }

        create_user(**payload)

        token_payload = {
            'email': payload['email'],
            'password': payload['password'],
        }

        res = self.client.post(TOKEN_URL, token_payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credentials(self):
        """Test token bad credentials"""
        payload = {
            'email': 'testuser@example.com',
            'password': 'password123',
            'name': 'Test Name',
        }

        create_user(**payload)

        token_payload = {
            'email': 'testuser@example.com',
            'password': '123password',
        }

        res = self.client.post(TOKEN_URL, token_payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_email_not_found(self):
        """Test create token without email"""
        token_payload = {
            'email': 'testuser10@example.com',
            'password': 'password123',
        }

        res = self.client.post(TOKEN_URL, token_payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_blank_password(self):
        """Test blank password error"""
        token_payload = {
            'email': 'testuser@example.com',
            'password': '',
        }

        res = self.client.post(TOKEN_URL, token_payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile_access_unauthorized(self):
        """Test profile access unauthorized error"""

        res = self.client.get(PROFILE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUseApiTests(TestCase):
    """Tests for authorized users"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = create_user(
            email='test@example.com',
            password='testpass123',
            name='Test Name',
        )

        self.client.force_authenticate(self.user)

    def test_retrieve_profile(self):
        """Test retrieve profile success"""

        res = self.client.get(PROFILE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'email': self.user.email,
            'name': self.user.name,
        })

    def test_update_profile(self):
        """Test update profile success"""

        payload = {
            'name': 'Update Test',
            'password': 'pass123test',
        }

        res = self.client.patch(PROFILE_URL, payload)

        self.user.refresh_from_db()

        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_to_profile(self):
        """Test post to profile error"""
        res = self.client.post(PROFILE_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
