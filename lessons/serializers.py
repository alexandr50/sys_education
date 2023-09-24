from rest_framework import serializers

from lessons.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Get lesson data with view details on it."""
    view_details = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'