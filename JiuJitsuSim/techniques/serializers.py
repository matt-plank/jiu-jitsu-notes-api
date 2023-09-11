from rest_framework import serializers

from . import models


class PositionSerializer(serializers.ModelSerializer):
    your_grips = serializers.StringRelatedField(many=True)
    their_grips = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Position
        fields = ["id", "name", "your_grips", "their_grips", "aspect"]


class PositionTechniquesSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    your_grips = serializers.StringRelatedField(many=True)
    their_grips = serializers.StringRelatedField(many=True)
    techniques = serializers.StringRelatedField(source="techniques_from", many=True)
    submissions = serializers.StringRelatedField(source="submissions_from", many=True)

    class Meta:
        model = models.Position
        fields = [
            "id",
            "name",
            "display_name",
            "your_grips",
            "their_grips",
            "aspect",
            "techniques",
            "submissions",
        ]

    def get_display_name(self, obj):
        return str(obj)


class TechniqueSerializer(serializers.ModelSerializer):
    from_position = PositionSerializer()
    to_position = PositionSerializer()

    class Meta:
        model = models.Technique
        fields = ["id", "name", "from_position", "to_position"]


class SubmissionTechniqueSerializer(serializers.ModelSerializer):
    from_position = PositionSerializer()

    class Meta:
        model = models.SubmissionTechnique
        fields = ["id", "name", "from_position"]


class GripSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grip
        fields = ["id", "name"]
