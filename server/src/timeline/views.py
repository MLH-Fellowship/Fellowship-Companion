from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Repository, Event
from .serializers import RepositorySerializer, EventSerializer
# Create your views here.


class RepositoryListView(generics.ListAPIView):
    queryset = Repository.objects.order_by('name')
    serializer_class = RepositorySerializer


class RepositoryDetailView(generics.RetrieveAPIView):
    serializer_class = RepositorySerializer

    def get(self, request, org, repo):
        queryset = Repository.objects.filter(fullname__iexact=f"{org}/{repo}")
        serializer = RepositorySerializer(queryset.first())
        return Response(serializer.data)


class EventListView(generics.ListAPIView):
    queryset = Event.objects.order_by('-created_at')
    serializer_class = EventSerializer
