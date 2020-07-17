from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
from .models import GithubUser
from .serializers import FellowListSerializer, FellowSerializer
# Create your views here.


class FellowListView(generics.ListAPIView):
    queryset = GithubUser.objects.filter(
        Q(teams__name__icontains="0.6.3") |
        Q(teams__name__icontains="0.6.2") |
        Q(teams__name__icontains="0.6.1") |
        Q(teams__name__icontains="0.5.2") |
        Q(teams__name__icontains="0.5.1") |
        Q(teams__name__icontains="0.4.2") |
        Q(teams__name__icontains="0.4.1") |
        Q(teams__name__icontains="0.3.2") |
        Q(teams__name__icontains="0.3.1") |
        Q(teams__name__icontains="0.2.2") |
        Q(teams__name__icontains="0.0.2") |
        Q(teams__name__icontains="0.1.2") |
        Q(teams__name__icontains="0.1.1") |
        Q(teams__name__icontains="0.0.1")
    ).distinct().exclude(
        Q(teams__name__icontains='MLH Staff') |
        Q(teams__name__icontains='Mentors')
    ).order_by('github_handle')
    queryset = queryset.exclude(Q(teams__name__icontains='MLH Staff') |
                                Q(teams__name__icontains='Mentors'))
    serializer_class = FellowListSerializer


class FellowDetailView(generics.RetrieveAPIView):
    serializer_class = FellowSerializer

    def get(self, request, github_handle):
        queryset = GithubUser.objects.filter(github_handle__iexact=github_handle)
        serializer = FellowSerializer(queryset.first())
        return Response(serializer.data)
