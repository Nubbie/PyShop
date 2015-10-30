from __future__ import absolute_import
from django import http

__author__ = 'Elfix'


def basket_info(request: http.HttpRequest):
    if request.user.is_authenticated():
        from customer.models import Customer
        from shop.models import OrderStatus, Order
        customer = Customer.objects.filter(pk=request.user.id).first()
        orders = Order.objects.filter(customer=customer,status=OrderStatus.IN_BASKET).count()
        if customer is not None:
            return {
                "order_count": orders
            }
    return {}
