from django.urls import path, include
from .views import FellowListView, FellowDetailView

urlpatterns = [
    path('', FellowListView.as_view()),
    path('<str:github_handle>/', FellowDetailView.as_view())
]
