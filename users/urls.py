from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, MyTokenObtainPairView
from rest_framework.routers import DefaultRouter


app_name = UsersConfig.name

# Описание маршрутизации для ViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view())
] + router.urls
