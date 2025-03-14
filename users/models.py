from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from datapush.validators import validate_email, validate_website



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, created_by="System", role=None, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            created_by=created_by,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,  
        )

        user.set_password(password)

        if role:
            user.role = role

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        # Ensure admin role exists or create it
        admin_role, _ = Role.objects.get_or_create(role_name=Role.ADMIN)
        return self.create_user(email, password, role=admin_role, is_staff=True, is_superuser=True)

# Role Model
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    ADMIN = 'Admin'
    NORMAL_USER = 'Normal user'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (NORMAL_USER, 'Normal user'),
    ]
    role_name = models.CharField(max_length=20, choices=ROLE_CHOICES, default=NORMAL_USER)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role_name

# Account Model
class Account(models.Model):
    account_name = models.CharField(max_length=250)
    app_secret_token = models.CharField(max_length=255, default=uuid.uuid4, editable=False)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=250)

    def __str__(self):
        return self.account_name


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(validators=[validate_email],unique=True)
    password = models.CharField(max_length=250)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=250)

    # Required fields for Django Admin
    is_active = models.BooleanField(default=True)      
    is_staff = models.BooleanField(default=False)      
    is_superuser = models.BooleanField(default=False)  # Superuser privileges

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email






