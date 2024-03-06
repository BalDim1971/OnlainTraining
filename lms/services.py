"""
Сервисные функции проведения оплаты курсов
"""

from config.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
import stripe


stripe.api_key = STRIPE_SECRET_KEY
