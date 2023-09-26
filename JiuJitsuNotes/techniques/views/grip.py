from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .. import db
from ..serializers import grip as grip_serializers


class GripView(APIView):
    """View for interacting with the grip model."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        grips = db.grip.all(request.user)
        result = grip_serializers.CompleteSerializer(grips, many=True).data

        return Response(result)

    def put(self, request):
        id = request.data["id"]
        grip = db.grip.find_by_id(request.user, id)

        grip.name = request.data["name"]
        grip.save()

        result = grip_serializers.CompleteSerializer(grip).data

        return Response(result)

    def post(self, request):
        name = request.data["name"]

        grip = db.grip.create(request.user, name)
        grip.save()

        result = grip_serializers.CompleteSerializer(grip).data

        return Response(result, status=201)

    def delete(self, request):
        id = request.data["id"]

        db.grip.delete_by_id(request.user, id)

        return Response(status=200)
