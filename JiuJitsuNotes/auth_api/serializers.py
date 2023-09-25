from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Serializes the User model."""

    class Meta:
        model = User
        fields = ["id", "username"]
