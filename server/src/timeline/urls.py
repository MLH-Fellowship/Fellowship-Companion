from django.urls import path
from .views import (
    RepositoryListView,
    RepositoryDetailView,
    EventListView
)

repository_urls = [
    path('', RepositoryListView.as_view()),
    path('<str:org>/<str:repo>/', RepositoryDetailView.as_view()),
]

event_urls = [
    path('', EventListView.as_view()),
]
