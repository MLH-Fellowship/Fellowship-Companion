from rest_framework import serializers
from .models import Repository


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
