from __future__ import absolute_import
from django import http

__author__ = 'Elfix'


def customer_info(request: http.HttpRequest):
    if request.user.is_authenticated():
        from customer.models import Customer
        customer = Customer.objects.filter(pk=request.user.id).first()
        if customer is not None:
            return {
                "customer": customer
            }
    return {}
