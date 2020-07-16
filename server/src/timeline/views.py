from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Repository
from .serializers import RepositorySerializer
# Create your views here.


class RepositoryListView(generics.ListAPIView):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
