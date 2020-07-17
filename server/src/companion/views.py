from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models import Q
from groups.models import GithubUser
from timeline.models import (
    Repository,
    PullRequest,
    Issue,
    Event,
)


class GetOverview(APIView):
    """
    View to get number of code lines contributed under MLH.
    """

    def get(self, request, format=None):
        """
        Return overview of fellowship.
        """
        response = {}
        response['loc'] = PullRequest.objects.aggregate(Sum('additions'))['additions__sum']
        fellows = GithubUser.objects.filter(
            Q(teams__name__icontains="0.6.3") |
            Q(teams__name__icontains="0.6.2") |
            Q(teams__name__icontains="0.6.1") |
            Q(teams__name__icontains="0.5.2") |
            Q(teams__name__icontains="0.5.1") |
            Q(teams__name__icontains="0.4.2") |
            Q(teams__name__icontains="0.4.1") |
            Q(teams__name__icontains="0.3.2") |
            Q(teams__name__icontains="0.3.1") |
            Q(teams__name__icontains="0.2.2") |
            Q(teams__name__icontains="0.0.2") |
            Q(teams__name__icontains="0.1.2") |
            Q(teams__name__icontains="0.1.1")
        ).distinct()
        response['fellows'] = fellows.count()
        response['projects'] = Repository.objects.all().count()
        return Response(response)
