from rest_framework import serializers
from .models import GithubUser, Team


class FellowTeamOverViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'description', 'avatar_url']


class FellowListSerializer(serializers.ModelSerializer):
    teams = FellowTeamOverViewSerializer(many=True)

    class Meta:
        model = GithubUser
        fields = [
            'name',
            'github_handle',
            'profile_url',
            'avatar_url',
            'location',
            'teams',
        ]


class FellowSerializer(serializers.ModelSerializer):
    teams = FellowTeamOverViewSerializer(many=True)

    class Meta:
        model = GithubUser
        fields = [
            'name',
            'github_handle',
            'avatar_url',
            'profile_url',
            'followers',
            'followers_url',
            'following',
            'following_url',
            'location',
            'teams'
        ]


class FellowOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubUser
        fields = [
            'name',
            'github_handle',
            'profile_url',
            'avatar_url',
        ]
