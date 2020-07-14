from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Fellow(models.Model):
    """
    A model for storing and handling fellows
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_handle = models.CharField(max_length=100)
    avatar_url = models.URLField()
