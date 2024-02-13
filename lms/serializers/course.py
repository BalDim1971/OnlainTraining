"""
Сериализатор для класса Курс
"""

from rest_framework import serializers

from lms.models import Course
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """
    Класс-сериализатор для курса.
    """

    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        return instance.lesson.count()
