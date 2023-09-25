from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response


class TokenView(APIView):
    """Represents the auth Token resource."""

    @permission_classes([AllowAny])
    def post(self, request):
        """Create and return a new auth token."""
        if "username" not in request.data:
            return Response({"error": "username not provided"}, status=status.HTTP_400_BAD_REQUEST)

        if "password" not in request.data:
            return Response({"error": "password not provided"}, status=status.HTTP_400_BAD_REQUEST)

        username: str = request.data["username"]
        password: str = request.data["password"]
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
