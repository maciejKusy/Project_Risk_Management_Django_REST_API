from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    """
    User do retain various data pertaining to the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    account_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username
