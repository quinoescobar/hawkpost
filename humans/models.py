from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        Project's base user model
    """
    public_key = models.TextField(blank=True, null=True)
    fingerprint = models.CharField(null=True, max_length=50)
    keyserver_url = models.URLField(null=True, blank=True)