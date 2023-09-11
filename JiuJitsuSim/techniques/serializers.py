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


class PositionTechniquesSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    your_grips = serializers.SerializerMethodField()
    their_grips = serializers.SerializerMethodField()
    techniques = serializers.SerializerMethodField()
    submissions = serializers.SerializerMethodField()

    class Meta:
        model = models.Position
        fields = ["name", "display_name", "your_grips", "their_grips", "aspect", "techniques", "submissions"]

    def get_display_name(self, obj):
        return str(obj)

    def get_your_grips(self, obj):
        return [grip.name for grip in obj.your_grips.all()]

    def get_their_grips(self, obj):
        return [grip.name for grip in obj.their_grips.all()]

    def get_techniques(self, obj) -> list[str]:
        return [technique.name for technique in obj.techniques_from.all()]

    def get_submissions(self, obj) -> list[str]:
        return [submission.name for submission in obj.submissions_from.all()]


class TechniqueSerializer(serializers.ModelSerializer):
    from_position = PositionSerializer()
    to_position = PositionSerializer()

    class Meta:
        model = models.Technique
        fields = ["name", "from_position", "to_position"]


class SubmissionTechniqueSerializer(serializers.ModelSerializer):
    from_position = PositionSerializer()

    class Meta:
        model = models.SubmissionTechnique
        fields = ["name", "from_position"]


class GripSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grip
        fields = ["id", "name"]
