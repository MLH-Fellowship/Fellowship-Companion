from django.contrib import admin
from .models import (
    Repository,
    Issue,
    PullRequest,
    Event,
)

# Register your models here.
admin.site.register(Repository)
admin.site.register(Issue)
admin.site.register(PullRequest)
admin.site.register(Event)
