from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    """
    Модель курса обучения
    """
    
    name = models.CharField(max_length=100, verbose_name='наименование')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='изображение', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    """
    Модель урока курса обучения
    """

    title = models.CharField(max_length=100, verbose_name='title')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    url = models.URLField(verbose_name='url', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'