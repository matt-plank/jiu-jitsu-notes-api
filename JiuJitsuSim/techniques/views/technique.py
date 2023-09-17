from rest_framework.views import APIView, Response

from .. import db
from ..models import Technique
from ..serializers import technique


class RandomTechniqueView(APIView):
    """Returns a random technique."""

    def get(self, request):
        random_technique: Technique = db.random_technique()

        result = technique.CompleteSerializer(random_technique).data

        return Response(result)


class TechniqueView(APIView):
    def put(self, request):
        instance: Technique = db.find_technique(request.data["id"])

        if "name" in request.data:
            instance.name = request.data["name"]

        if "from_position" in request.data:
            instance.from_position = db.find_position(request.data["from_position"]["id"])

        if "to_position" in request.data:
            instance.to_position = db.find_position(request.data["to_position"]["id"])

        result = technique.CompleteSerializer(instance).data

        return Response(result)

    def post(self, request):
        instance: Technique = Technique.objects.create(
            name=request.data["name"],
            from_position=db.find_position(request.data["from_position"]["id"]),
            to_position=db.find_position(request.data["to_position"]["id"]),
        )

        result = technique.CompleteSerializer(instance).data

        return Response(result)
