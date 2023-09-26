from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from .. import db
from ..models import SubmissionTechnique
from ..serializers import submission


class RandomSubmissionView(APIView):
    """Returns a random submission."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        random_submission: SubmissionTechnique = db.submission.get_random(request.user)

        result = submission.CompleteSerializer(random_submission).data

        return Response(result)


class SubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        instance: SubmissionTechnique = db.submission.find_by_id(
            request.user,
            request.data["id"],
        )

        if "name" in request.data:
            instance.name = request.data["name"]

        if "from_position" in request.data:
            instance.from_position = db.position.find_by_id(
                request.user,
                request.data["from_position"]["id"],
            )

        instance.save()

        result = submission.CompleteSerializer(instance).data

        return Response(result)

    def post(self, request):
        from_position = db.position.find_by_id(
            request.user,
            request.data["from_position"]["id"],
        )

        instance: SubmissionTechnique = db.submission.create(
            request.user,
            request.data["name"],
            from_position,
        )

        result = submission.CompleteSerializer(instance).data

        return Response(result)

    def delete(self, request):
        instance: SubmissionTechnique = db.submission.find_by_id(
            request.user,
            request.data["id"],
        )

        instance.delete()

        return Response(status=200)
