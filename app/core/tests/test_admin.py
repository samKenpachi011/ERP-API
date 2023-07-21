"""
Tests for the admmin site
"""
from django.test import TestCase, Client
from core.helpers import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Tests for the admin site"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='password123'
        )

        self.client.force_login(self.admin_user)

        # normal user
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='password123'
        )

    def test_admin_list_users(self):
        """Test listing users on page"""

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_edit_user(self):
        """Test the edit user page"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_add_user(self):
        """Test the add user page"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
