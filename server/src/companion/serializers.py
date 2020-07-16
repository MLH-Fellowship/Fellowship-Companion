from rest_framework import serializers, pagination
from rest_framework.response import Response


class OverviewSerializer(serializers.Serializer):
    loc = serializers.IntegerField()
    members = serializers.IntegerField()
    repositories = serializers.IntegerField()


class CustomPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
