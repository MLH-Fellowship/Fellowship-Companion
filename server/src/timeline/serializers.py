from rest_framework import serializers
from .models import Repository, Event, Issue, PullRequest
from groups.serializers import FellowListSerializer


class RepositorySerializer(serializers.ModelSerializer):
    contributors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='github_handle'
    )

    class Meta:
        model = Repository
        fields = [
            'name',
            'fullname',
            'description',
            'url',
            'contributed_loc',
            'contributors',
        ]


class RepoOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = [
            'name',
            'organization',
            'url',
        ]


class IssueOverviewSerializer(serializers.ModelSerializer):
    related_pr = serializers.IntegerField('get_pr_number')

    class Meta:
        model = Issue
        fields = [
            'title',
            'url',
            'number',
            'related_pr'
        ]


class PROverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest
        fields = [
            'title',
            'url',
            'merged',
            'number',
            'additions',
            'deletions'
        ]


class EventSerializer(serializers.ModelSerializer):
    issue = IssueOverviewSerializer(many=False)
    pull_request = PROverviewSerializer(many=False)
    user = FellowListSerializer(many=False)
    repository = RepoOverviewSerializer(many=False)

    class Meta:
        model = Event
        fields = [
            'type',
            'action',
            'created_at',
            'issue',
            'pull_request',
            'user',
            'repository',
        ]
