from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .. import db, models
from ..serializers import grip as grip_serializers


class GripView(APIView):
    """View for interacting with the grip model."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        grips = db.all_grips()
        result = grip_serializers.CompleteSerializer(grips, many=True).data

        return Response(result)

    def put(self, request):
        id = request.data["id"]
        grip = db.find_grip(id)

        grip.name = request.data["name"]
        grip.save()

        result = grip_serializers.CompleteSerializer(grip).data

        return Response(result)

    def post(self, request):
        name = request.data["name"]

        grip = models.Grip(name=name)
        grip.save()

        result = grip_serializers.CompleteSerializer(grip).data

        return Response(result, status=201)

    def delete(self, request):
        id = request.data["id"]

        db.delete_grip(id)

        return Response(status=200)
