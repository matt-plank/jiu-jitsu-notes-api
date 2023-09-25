from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response

from .. import db
from ..models import Position
from ..serializers import position as position_serializers


def update_property_from_request(instance, request_data, property: str):
    """(Optionally) updates a given model property if it is provided in the request data."""
    if property not in request_data:
        return

    setattr(instance, property, request_data[property])


def update_grips_from_request(instance, request_data, grip_relation_name: str):
    """Copies a list of grips into a position."""
    if grip_relation_name not in request_data:
        return

    instance_grips = getattr(instance, grip_relation_name)
    instance_grips.clear()

    for grip in request_data[grip_relation_name]:
        grip_id: int = grip["id"]
        instance_grips.add(db.find_grip(grip_id))


class PositionsView(APIView):
    """Returns a list of all positions - and the techniques originating from each position."""

    permission_classes = [IsAuthenticated]

    def get_single(self, request: Request):
        """GET a single position."""
        position = Position.objects.get(pk=request.query_params["id"])
        result = position_serializers.CompleteSerializer(position).data

        return Response(result)

    def get_many(self, request: Request):
        """GET all positions."""
        positions = db.all_positions()
        result = position_serializers.CompleteSerializer(positions, many=True).data

        return Response(result)

    def get(self, request: Request):
        """Handle GET request. Return either a single position or a list of positions depending on URL args."""
        if "id" in request.query_params:
            return self.get_single(request)

        return self.get_many(request)

    def put(self, request):
        """Updates a given position with new details, returns the new serialized data for that position."""
        if "id" not in request.data:
            return Response("ID required", status=400)

        for grip in request.data.get("your_grips", []):
            if "id" not in grip:
                return Response("Grip ID required", status=400)

        position = db.find_position(id=request.data["id"])

        update_property_from_request(position, request.data, "aspect")
        update_property_from_request(position, request.data, "name")
        update_grips_from_request(position, request.data, "your_grips")
        update_grips_from_request(position, request.data, "their_grips")

        position.save()

        result = position_serializers.CompleteSerializer(position).data

        return Response(result)

    def post(self, request):
        """Creates a new position with given details, returns the serialized data for the new position."""
        if "name" not in request.data:
            return Response("Position name required", status=400)

        if "aspect" not in request.data:
            return Response("Position aspect required", status=400)

        for grip in request.data.get("your_grips", []):
            if "id" not in grip:
                return Response("Grip ID requred", status=400)

        for grip in request.data.get("their_grips", []):
            if "id" not in grip:
                return Response("Grip ID requred", status=400)

        position = Position.objects.create(
            name=request.data["name"],
            aspect=request.data["aspect"],
        )

        update_grips_from_request(position, request.data, "your_grips")
        update_grips_from_request(position, request.data, "their_grips")

        result = position_serializers.CompleteSerializer(position).data

        return Response(result)

    def delete(self, request):
        """Deletes a given position. Returns status 200 if completed."""
        if "id" not in request.data:
            return Response("ID required", status=400)

        position = db.find_position(id=request.data["id"])

        position.delete()

        return Response(status=200)
