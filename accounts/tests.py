from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import AccountMember
from users.models import Account, User, Role


class AccountMemberModelTests(TestCase):

    def setUp(self):
        self.account = Account.objects.create(
            account_name='Test Account',
            app_secret_token='testtoken',
            website='https://example.com',
        )
        self.role = Role.objects.create(
            role_name='Admin'
        )
        self.user = User.objects.create(
            email='testuser@example.com',
            password='testpass123',
            account = self.account,
            role = self.role
        )
        self.account_member = AccountMember.objects.create(
            user=self.user,
            role=self.role,
            account = self.account
        )

    def test_create_account_member(self):
        # Test account member creation
        self.assertEqual(self.account_member.user, self.user)
        self.assertEqual(self.account_member.role.role_name, self.role.role_name)

    def test_account_member_role(self):
        # Test account member role
        self.account_member.role = self.role
        self.account_member.save()
        self.assertEqual(self.account_member.role.role_name, self.role.role_name)
