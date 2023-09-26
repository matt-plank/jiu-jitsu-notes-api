from rest_framework import serializers

from .. import models
from . import grip


class PositionDetails(serializers.ModelSerializer):
    display_name = serializers.StringRelatedField(source="__str__")
    your_grips = grip.CompleteSerializer(many=True)
    their_grips = grip.CompleteSerializer(many=True)

    class Meta:
        model = models.Position
        fields = ["id", "aspect", "name", "display_name", "your_grips", "their_grips"]


class ToPositionPartialSerializer(serializers.ModelSerializer):
    to_position = PositionDetails()

    class Meta:
        model = models.Technique
        fields = ["id", "name", "to_position"]


class CompleteSerializer(serializers.ModelSerializer):
    from_position = PositionDetails()
    to_position = PositionDetails()

    class Meta:
        model = models.Technique
        exclude = ("user",)
