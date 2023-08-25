from rest_framework import serializers

from . import models


class PositionSerializer(serializers.ModelSerializer):
    your_grips = serializers.SerializerMethodField()
    their_grips = serializers.SerializerMethodField()

    class Meta:
        model = models.Position
        fields = ["name", "your_grips", "their_grips", "aspect"]

    def get_your_grips(self, obj):
        return [grip.name for grip in obj.your_grips.all()]

    def get_their_grips(self, obj):
        return [grip.name for grip in obj.their_grips.all()]


class TechniqueSerializer(serializers.ModelSerializer):
    from_position = PositionSerializer()
    to_position = PositionSerializer()

    class Meta:
        model = models.Technique
        fields = ["name", "from_position", "to_position"]
