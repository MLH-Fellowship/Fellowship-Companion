from rest_framework import serializers
from .models import GithubUser, Team


class FellowTeeamOverViewSerialier(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'description']


class FellowListSerializer(serializers.ModelSerializer):
    teams = FellowTeeamOverViewSerialier(many=True)

    class Meta:
        model = GithubUser
        fields = ['name', 'github_handle', 'avatar_url',
                  'location', 'teams']


class FellowSerializer(serializers.ModelSerializer):
    teams = FellowTeeamOverViewSerialier(many=True)

    class Meta:
        model = GithubUser
        fields = [
            'name',
            'github_handle',
            'avatar_url',
            'followers',
            'followers_url',
            'following',
            'following_url',
            'location',
            'teams'
        ]
