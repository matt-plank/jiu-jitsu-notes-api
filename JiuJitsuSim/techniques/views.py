from rest_framework.views import APIView, Response

from . import db, models, serializers


class RandomTechniqueView(APIView):
    """Returns a random technique."""

    def get(self, request):
        random_technique: models.Technique = db.random_technique()

        result = serializers.TechniqueSerializer(random_technique).data

        return Response(result)


class RandomSubmissionView(APIView):
    """Returns a random submission."""

    def get(self, request):
        random_submission: models.SubmissionTechnique = db.random_submission()

        result = serializers.SubmissionTechniqueSerializer(random_submission).data

        return Response(result)


class PositionsView(APIView):
    """Returns a list of all positions - and the techniques originating from each position."""

    def get(self, request):
        positions = db.all_positions()
        result = serializers.PositionTechniquesSerializer(positions, many=True).data

        return Response(result)


class GripView(APIView):
    """View for interacting with the grip model."""

    def get(self, request):
        grips = db.all_grips()
        result = serializers.GripSerializer(grips, many=True).data

        return Response(result)

    def put(self, request):
        id = request.data["id"]
        grip = db.find_grip(id)

        grip.name = request.data["name"]
        grip.save()

        result = serializers.GripSerializer(grip).data

        return Response(result)
