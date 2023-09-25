from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

from .serializers import UserSerializer


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


class AccountView(APIView):
    """Represents the account resource."""

    @permission_classes([AllowAny])
    def post(self, request):
        """Create a new user account."""
        if "username" not in request.data:
            return Response(
                {"error": "username not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if "password" not in request.data:
            return Response(
                {"error": "password not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        username: str = request.data["username"]
        password: str = request.data["password"]

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "username already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(
            username=username,
            password=password,
        )

        result = UserSerializer(user).data

        return Response(result, status=status.HTTP_201_CREATED)
