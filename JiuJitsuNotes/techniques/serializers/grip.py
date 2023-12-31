from rest_framework import serializers

from .. import models


class CompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grip
        exclude = ("user",)
