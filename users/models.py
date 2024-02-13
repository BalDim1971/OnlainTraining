from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from lms.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Класс, описывающий модель пользователь
    Стандартная модель расширяется:
    «Аватар»,
    «Номер телефона»,
    «Страна».
    Авторизация меняется на email
    """
    username = None
    email = models.EmailField(max_length=200, verbose_name='электронная почта',
                              unique=True)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар',
                               **NULLABLE)
    city = models.CharField(max_length=150, verbose_name='город', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Payment(models.Model):
    """
    Модель платежей:
    пользователь,
    дата оплаты,
    оплаченный курс или урок,
    сумма оплаты,
    способ оплаты: наличные или перевод на счет.
    """
    PAYMENT_CHOICE = [
        ('cash', 'наличными'),
        ('card', 'картой'),
    ]
    user = models.ForeignKey(User, on_delete=CASCADE,
                             verbose_name='пользователь')
    date_of_payment = models.DateField(verbose_name='дата платежа')
    paid_lesson = models.ForeignKey(Lesson, on_delete=CASCADE, **NULLABLE,
                                    verbose_name='оплаченный урок')
    paid_course = models.ForeignKey(Course, on_delete=CASCADE, **NULLABLE,
                                    verbose_name='оплаченный курс')
    amount_payment = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name='сумма оплаты')
    method_payment = models.CharField(max_length=10, choices=PAYMENT_CHOICE,
                                      verbose_name='метод оплаты')

    def __str__(self):
        return f'{self.user} оплатил {self.date_of_payment}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
