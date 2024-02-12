"""
Сериаизаторы для класса Курс
"""

from rest_framework import serializers

from lms.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для курса.
    """

    count_lesson = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lesson(self, obj):
        return obj.lesson.count()
