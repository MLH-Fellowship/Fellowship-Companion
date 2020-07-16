from django.urls import path
from .views import RepositoryListView, RepositoryDetailView

repository_urls = [
    path('', RepositoryListView.as_view()),
    path('<str:org>/<str:repo>/', RepositoryDetailView.as_view()),
]
