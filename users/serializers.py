from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор платежей
    """
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя
    """
    date_joined = serializers.DateTimeField(format="%Y-%m-%d")
    
    history_payment = PaymentSerializer(many=True, read_only=True,
                                        source='payment_set')

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'avatar',
            'city',
            'is_staff',
            'is_active',
            'date_joined',
            'history_payment'
        ]
