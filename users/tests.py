from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='testuser@example.com',
            password='testpass123'
        )

    def test_create_user(self):
        # Test user creation
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

  

    def test_delete_user(self):
        # Test user deletion
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(self.User.DoesNotExist):
            self.User.objects.get(id=user_id)

    def test_user_email_unique(self):
        # Test email uniqueness
        with self.assertRaises(Exception):
            self.User.objects.create_user(
                email='testuser@example.com',
                password='testpass123'
            )

    def test_create_superuser(self):
        # Test superuser creation
        superuser = self.User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)


class AccountsModelTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            email='testuser@example.com',
            password='testpass123'
        )

    def test_create_user(self):
        # Test user creation
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_user_email_unique(self):
        # Test email uniqueness
        with self.assertRaises(Exception):
            self.User.objects.create_user(
                email='testuser@example.com',
                password='testpass123'
            )

    def test_create_superuser(self):
        # Test superuser creation
        superuser = self.User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

