from django.db import models
from groups.models import Fellow


class Repository(models.Model):
    """
    A model to store and handle repositories to which fellows are contributing
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    contributed_loc = models.BigIntegerField()

    def __str__(self):
        return self.name


class Issue(models.Model):
    """
    A model to keep an eye on the repository's issues
    """
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=10)
    url = models.URLField()
    user = models.ForeignKey(to=Fellow, on_delete=models.CASCADE)
    repo = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PullRequest(models.Model):
    """
    A model to keep an eye on the repository's pull requests
    """
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    status = models.CharField(max_length=10)
    url = models.URLField()
    additions = models.BigIntegerField()
    deletions = models.BigIntegerField()
    user = models.ForeignKey(to=Fellow, on_delete=models.CASCADE)
    repo = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    A model for handling different events occurring under an organization
    """
    PR = 'PR'
    ISSUE = 'IS'
    CREATE = 'CR'
    EVENT_TYPE_CHOICES = [
        (PR, 'pull_request'),
        (ISSUE, 'issue'),
        (CREATE, 'create')
    ]
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField()
    type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES)
    issue = models.ForeignKey(to=Issue, null=True, blank=True, on_delete=models.CASCADE)
    pull_request = models.ForeignKey(to=PullRequest, null=True,
                                     blank=True, on_delete=models.CASCADE)
    repository = models.ForeignKey(to=Repository, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} ({self.id})"
