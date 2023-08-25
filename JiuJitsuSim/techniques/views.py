from rest_framework.views import APIView, Response

from . import db, models, serializers


class RandomTechniqueView(APIView):
    """Returns a random technique."""

    def get(self, request):
        random_technique: models.Technique = db.random_technique()

        result = serializers.TechniqueSerializer(random_technique).data

        return Response(result)
