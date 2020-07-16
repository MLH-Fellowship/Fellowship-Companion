from django.urls import path, include
from .views import RepositoryListView

repository_urls = [
    path('', RepositoryListView.as_view()),
]
