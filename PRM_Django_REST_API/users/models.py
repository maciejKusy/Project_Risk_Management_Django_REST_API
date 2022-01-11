from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    account_created = models.DateTimeField(default=timezone.now)
    projects = models.ManyToManyField('projects.Project', related_name='users_assigned', blank=True)

    def __str__(self):
        return self.user.username
