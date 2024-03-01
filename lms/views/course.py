from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from lms.models import Course
from lms.paginations.course import CoursePagination
from lms.permissions import IsOwnerOrStaff
from lms.serializers.course import CourseSerializer
from users.permissions import IsOwner, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    queryset = Course.objects.all()

    def get_permissions(self):
        """
        Определяем права доступа по запрашиваемому действию
        :return: Уровень доступа
        """
        match self.action:
            case 'create':
                self.permission_classes = [IsAuthenticated, ~IsModerator]
            case 'destroy':
                self.permission_classes = [IsAuthenticated, IsOwner]
            case _:  # ['list', 'retrieve', 'update']
                self.permission_classes = [IsAuthenticated, IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        """
        Привязать пользователя к созданному курсу
        """
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
