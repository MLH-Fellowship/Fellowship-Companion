from django.urls import path
from .views import GetCodeLines

urlpatterns = [
    path('lines/', GetCodeLines.as_view())
]
