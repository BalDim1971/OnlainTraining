from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payments.models import Payment
from payments.serializers import PaymentSerializer


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


