from rest_framework.views import APIView, Response

from .. import db
from ..models import Position
from ..serializers import position as position_serializers


class PositionsView(APIView):
    """Returns a list of all positions - and the techniques originating from each position."""

    def get(self, request):
        positions = db.all_positions()
        result = position_serializers.CompleteSerializer(positions, many=True).data

        return Response(result)

    def put(self, request):
        position = db.find_position(id=request.data["id"])

        if "aspect" in request.data:
            position.aspect = request.data["aspect"]

        if "name" in request.data:
            position.name = request.data["name"]

        if "your_grips" in request.data:
            position.your_grips.clear()

            your_grips: list[dict] = request.data["your_grips"]

            for grip in your_grips:
                grip_id: int = grip["id"]
                position.your_grips.add(db.find_grip(grip_id))

        if "their_grips" in request.data:
            position.their_grips.clear()

            their_grips: list[dict] = request.data["their_grips"]

            for grip in their_grips:
                grip_id: int = grip["id"]
                position.their_grips.add(db.find_grip(grip_id))

        position.save()

        result = position_serializers.CompleteSerializer(position).data

        return Response(result)

    def post(self, request):
        position = Position.objects.create(
            name=request.data["name"],
            aspect=request.data["aspect"],
        )

        for grip_data in request.data.get("your_grips", []):
            grip = db.find_grip(grip_data["id"])
            position.your_grips.add(grip)

        for grip_data in request.data.get("their_grips", []):
            grip = db.find_grip(grip_data["id"])
            position.their_grips.add(grip)

        result = position_serializers.CompleteSerializer(position).data

        return Response(result)

    def delete(self, request):
        position = db.find_position(id=request.data["id"])

        position.delete()

        return Response(status=200)
