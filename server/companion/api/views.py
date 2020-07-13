from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class GetCodeLines(APIView):
    """
    View to get number of code lines contributed under MLH.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        response = {'lines': 1234567894546}
        return Response(response)
