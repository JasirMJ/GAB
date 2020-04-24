from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from Chat.models import Questions


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"
