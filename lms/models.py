"""
Файл с описанием моделей по курсу обучения и урокам.
"""

from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    """
    Модель курса обучения
    """

    name = models.CharField(max_length=100, verbose_name='наименование')
    preview = models.ImageField(upload_to='course_previews/',
                                verbose_name='картинка',
                                **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ['name',]
        indexes = [
            models.Index(fields=['name']),
        ]


class Lesson(models.Model):
    """
    Модель урока курса обучения
    """

    name = models.CharField(max_length=100, verbose_name='название урока')
    preview = models.ImageField(upload_to='lesson_previews/',
                                verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(verbose_name='видеоурок', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='курс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ['course', 'name',]
