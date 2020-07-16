from rest_framework import routers, serializers, viewsets


class OverviewSerializer(serializers.Serializer):
    loc = serializers.IntegerField()
    members = serializers.IntegerField()
    repositories = serializers.IntegerField()
