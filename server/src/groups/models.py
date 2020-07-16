from django.db import models

# Create your models here.


class Team(models.Model):
    """
    A model to handle teams under organizations
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    avatar_url = models.URLField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class GithubUser(models.Model):
    """
    A model for storing and handling fellows, staff and mentors
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    github_handle = models.CharField(max_length=100)
    avatar_url = models.URLField()
    location = models.CharField(max_length=100, null=True, blank=True)
    followers = models.PositiveIntegerField()
    followers_url = models.URLField()
    following = models.PositiveIntegerField()
    following_url = models.URLField()
    teams = models.ManyToManyField(to=Team)
    loc = models.IntegerField(default=0)

    def __str__(self):
        return self.github_handle
