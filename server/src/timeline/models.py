from django.db import models
from groups.models import GithubUser


class Repository(models.Model):
    """
    A model to store and handle repositories to which fellows are contributing
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    contributed_loc = models.BigIntegerField(default=0)
    contributors = models.ManyToManyField(to=GithubUser)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class PullRequest(models.Model):
    """
    A model to keep an eye on the repository's pull requests
    """
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=10)
    url = models.URLField()
    additions = models.BigIntegerField()
    deletions = models.BigIntegerField()
    user = models.ForeignKey(to=GithubUser, on_delete=models.CASCADE)
    repo = models.ForeignKey(to=Repository, on_delete=models.CASCADE)
    merged = models.BooleanField()

    def __str__(self):
        return self.url


class Issue(models.Model):
    """
    A model to keep an eye on the repository's issues
    """
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True, blank=True)
    state = models.CharField(max_length=10)
    url = models.URLField()
    related_pr = models.ForeignKey(to=PullRequest, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to=GithubUser, on_delete=models.CASCADE, null=True)
    repo = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    A model for handling different events occurring under an organization
    """
    PR = 'PR'
    ISSUE = 'IS'
    FORK = 'FK'
    EVENT_TYPE_CHOICES = [
        (PR, 'pull_request'),
        (ISSUE, 'issue'),
        (FORK, 'fork')
    ]
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES)
    action = models.CharField(max_length=20)
    issue = models.ForeignKey(to=Issue, null=True, blank=True, on_delete=models.CASCADE)
    pull_request = models.ForeignKey(to=PullRequest, null=True,
                                     blank=True, on_delete=models.CASCADE)
    repository = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} ({self.id})"
