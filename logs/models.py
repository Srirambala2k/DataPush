from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
from accounts.models import Account
from destinations.models import Destination



# Create your models here.
class Log(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    destination = models.ForeignKey('destinations.Destination', on_delete=models.CASCADE)
    received_timestamp = models.DateTimeField()
    processed_timestamp = models.DateTimeField()
    received_data = models.JSONField()
    status = models.CharField(max_length=20)  # e.g., 'success', 'failed'

    def __str__(self):
        return f"Log {self.event_id} - {self.status}"

