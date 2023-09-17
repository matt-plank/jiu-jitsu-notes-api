from rest_framework.views import APIView, Response

from .. import db, models
from ..serializers import submission


class RandomSubmissionView(APIView):
    """Returns a random submission."""

    def get(self, request):
        random_submission: models.SubmissionTechnique = db.random_submission()

        result = submission.CompleteSerializer(random_submission).data

        return Response(result)
