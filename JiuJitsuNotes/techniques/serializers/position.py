from rest_framework import serializers

from .. import models
from . import grip, submission, technique


class CompleteSerializer(serializers.ModelSerializer):
    display_name = serializers.StringRelatedField(source="__str__")
    your_grips = grip.CompleteSerializer(many=True)
    their_grips = grip.CompleteSerializer(many=True)
    techniques = technique.ToPositionPartialSerializer(source="techniques_from", many=True)
    submissions = submission.PartialSerializer(source="submissions_from", many=True)

    class Meta:
        model = models.Position
        fields = "__all__"