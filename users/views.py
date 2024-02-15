from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ViewSet):
    """
    Простой ViewSet-класс для вывода списка пользователей и
    информации по одному объекту
    """

    def list(self, request):
        """
        Метод для вывода списка пользователей с определением выборки
        из базы и указанием сериализатора
        :param request:
        :return:
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Метод для вывода информации по пользователю с определением выборки
        из базы и указанием сериализатора
        :param self:
        :param request:
        :param pk:
        :return:
        """
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PaymentListApiView(generics.ListAPIView):
    """
    Класс для формирования списка платежей
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    search_fields = ['paid_lesson', 'paid_course', 'method_payment']
    ordering_fields = ('date_of_payment',)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_lesson', 'paid_course', 'method_payment')
