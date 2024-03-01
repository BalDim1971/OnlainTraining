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
    lesson = LessonSerializer(source='lessons', many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description',
                  'lesson_count', 'lesson']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Course.objects.all(),
                fields=['name',],
                message='Имя курса должно быть уникальным'
            )
        ]

    def get_lesson_count(self, instance):
        return instance.lessons.count()
