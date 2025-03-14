from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from datapush.validators import validate_email, validate_website
from users.models import User, Role, Account




class AccountMember(models.Model):
    account = models.ForeignKey('users.Account', on_delete=models.CASCADE, related_name='account_members')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_accounts')
    role = models.ForeignKey('users.Role', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=250)
    updated_by = models.CharField(max_length=250)

    class Meta:
        unique_together = ('account', 'user')  # Ensure a user can be added only once per account

    def __str__(self):
        return f"{self.user.email} - {self.account.account_name} ({self.role.role_name})"

    def get_user_role(self):
        from users.models import User
        return User.objects.filter(account=self).first().role.role_name
