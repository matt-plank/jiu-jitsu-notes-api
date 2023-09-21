from rest_framework.views import APIView, Response

from .. import db
from ..models import SubmissionTechnique
from ..serializers import submission


class RandomSubmissionView(APIView):
    """Returns a random submission."""

    def get(self, request):
        random_submission: SubmissionTechnique = db.random_submission()

        result = submission.CompleteSerializer(random_submission).data

        return Response(result)


class SubmissionView(APIView):
    def put(self, request):
        instance: SubmissionTechnique = SubmissionTechnique.objects.get(pk=request.data["id"])

        if "name" in request.data:
            instance.name = request.data["name"]

        if "from_position" in request.data:
            instance.from_position = db.find_position(request.data["from_position"]["id"])

        instance.save()

        result = submission.CompleteSerializer(instance).data

        return Response(result)

    def post(self, request):
        instance: SubmissionTechnique = SubmissionTechnique.objects.create(
            name=request.data["name"],
            from_position=db.find_position(request.data["from_position"]["id"]),
        )

        result = submission.CompleteSerializer(instance).data

        return Response(result)

    def delete(self, request):
        instance: SubmissionTechnique = SubmissionTechnique.objects.get(pk=request.data["id"])

        instance.delete()

        return Response(status=200)
