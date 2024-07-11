from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('', testing),
    path('confirm_order', create_order, name = 'create_order'),
    path('payment_status', payment_status, name = 'payment_status'),
    path('confirm_cash_on_delivery/', confirm_cash_on_delivery, name='confirm_cash_on_delivery'),
    path('confirm-online-payment/', confirm_online_payment, name='confirm_online_payment'),
    path('handle_confirm_order/', handle_confirm_order, name='handle_confirm_order'),
    # path('payments/', include('payments.urls')),
]

