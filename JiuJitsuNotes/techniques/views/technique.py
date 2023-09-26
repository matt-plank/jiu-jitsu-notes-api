from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .. import db
from ..models import Technique
from ..serializers import technique


class RandomTechniqueView(APIView):
    """Returns a random technique."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        random_technique: Technique = db.technique.get_random(request.user)
        result = technique.CompleteSerializer(random_technique).data

        return Response(result)


class TechniqueView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        instance: Technique = db.technique.find_by_id(request.user, request.data["id"])

        if "name" in request.data:
            instance.name = request.data["name"]

        if "from_position" in request.data:
            instance.from_position = db.position.find_by_id(request.user, request.data["from_position"]["id"])

        if "to_position" in request.data:
            instance.to_position = db.position.find_by_id(request.user, request.data["to_position"]["id"])

        instance.save()

        result = technique.CompleteSerializer(instance).data

        return Response(result)

    def post(self, request):
        from_position = db.position.find_by_id(request.user, request.data["from_position"]["id"])
        to_position = db.position.find_by_id(request.user, request.data["to_position"]["id"])

        instance: Technique = db.technique.create(
            request.user,
            request.data["name"],
            from_position,
            to_position,
        )

        result = technique.CompleteSerializer(instance).data

        return Response(result)

    def delete(self, request):
        instance: Technique = db.technique.find_by_id(request.user, request.data["id"])

        instance.delete()

        return Response(status=200)
