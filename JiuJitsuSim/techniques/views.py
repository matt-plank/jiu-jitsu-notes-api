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

    def put(self, request):
        position = db.find_position(id=request.data["id"])

        if "aspect" in request.data:
            position.aspect = request.data["aspect"]

        if "name" in request.data:
            position.name = request.data["name"]

        if "your_grips" in request.data:
            position.your_grips.clear()

            your_grips: dict = dict(request.data)["your_grips"]

            for grip in your_grips:
                position.your_grips.add(db.find_grip_from_name(grip))

        if "their_grips" in request.data:
            position.their_grips.clear()

            their_grips: dict = dict(request.data)["their_grips"]

            for grip in their_grips:
                position.their_grips.add(db.find_grip_from_name(grip))

        position.save()

        result = serializers.PositionTechniquesSerializer(position).data

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

    def post(self, request):
        name = request.data["name"]

        grip = models.Grip(name=name)
        grip.save()

        result = serializers.GripSerializer(grip).data

        return Response(result, status=201)

    def delete(self, request):
        id = request.data["id"]

        db.delete_grip(id)

        return Response(status=200)
