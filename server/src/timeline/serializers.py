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
    related_pr = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Issue
        fields = [
            'title',
            'url',
            'number',
            'related_pr'
        ]

    def get_related_pr(self, issue):
        return issue.related_pr.number if issue.related_pr else None


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
    issue = IssueOverviewSerializer(many=False, read_only=True)
    pull_request = PROverviewSerializer(many=False, read_only=True)
    user = FellowListSerializer(many=False, read_only=True)
    repository = RepoOverviewSerializer(many=False, read_only=True)

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
