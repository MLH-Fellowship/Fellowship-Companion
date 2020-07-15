from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    """
    A model to handle teams under organizations
    """
    name = models.CharField(max_length=100)
    avatar_url = models.URLField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Fellow(models.Model):
    """
    A model for storing and handling fellows
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    github_handle = models.CharField(max_length=100)
    avatar_url = models.URLField()
    team = models.ManyToManyField(to=Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name
