from django.contrib import admin
from .models import GithubUser, Team

# Register your models here.
admin.site.register(GithubUser)
admin.site.register(Team)
