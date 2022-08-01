import random

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class UserView(GenericViewSet):
    def get(self, request):
        """Dummy implementation of the API"""

        return Response(
            data=dict(
                user=random.choice(("I", "me", "myself")),
            ),
            status=status.HTTP_200_OK,
        )
