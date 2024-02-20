from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from lms.models import Course
from lms.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
