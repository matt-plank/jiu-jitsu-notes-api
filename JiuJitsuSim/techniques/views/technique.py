from rest_framework.views import APIView, Response

from .. import db, models
from ..serializers import technique


class RandomTechniqueView(APIView):
    """Returns a random technique."""

    def get(self, request):
        random_technique: models.Technique = db.random_technique()

        result = technique.CompleteSerializer(random_technique).data

        return Response(result)
