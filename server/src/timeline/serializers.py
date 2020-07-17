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
            'avatar_url',
            'contributed_loc',
            'contributors',
        ]


class RepoOverviewSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Repository
        fields = [
            'name',
            'organization',
            'url',
            'avatar_url',
        ]

    def get_organization(self, repo):
        return repo.fullname.split('/')[0]


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
    user = serializers.SerializerMethodField(read_only=True)
    repository = serializers.SerializerMethodField(read_only=True)

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

    def get_user(self, event):
        if event.issue is None:
            return FellowListSerializer(event.pull_request.user).data
        else:
            return FellowListSerializer(event.issue.user).data

    def get_repository(self, event):
        if event.issue is None:
            return RepoOverviewSerializer(event.pull_request.repo).data
        else:
            return RepoOverviewSerializer(event.issue.repo).data
