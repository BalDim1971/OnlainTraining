from django.urls import path

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentListApiView
from rest_framework.routers import DefaultRouter


app_name = UsersConfig.name

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('payment/', PaymentListApiView.as_view(), name='payment_list'),
] + router.urls
