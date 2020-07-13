from django.urls import path
from .views import GetLOCView

urlpatterns = [
    path('loc/', GetLOCView.as_view())
]
