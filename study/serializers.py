from rest_framework import serializers
from adminPanel.models import SubtopicModel

class SubtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtopicModel
        fields = ("__all__")