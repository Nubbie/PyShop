from __future__ import absolute_import
from django.conf.urls import url
from shop.views import Homepage, AddToBasket, Checkout, RemoveFromBasket, GotoBank, BackFromBank, History

__author__ = 'Elfix'

urlpatterns = [
    url(r'add-to-basket', AddToBasket.as_view(), name="order"),
    url(r'delete-from-basket/(?P<pk>\d+)/?', RemoveFromBasket.as_view(), name="unorder"),
    url(r'basket', Checkout.as_view(), name="basket"),
    url(r'history', History.as_view(), name="history"),
    url(r'bank/Go-To-Bank', GotoBank.as_view(), name="bank"),
    url(r'bank/Back', BackFromBank.as_view(), name="back-from-bank"),
    url(r'', Homepage.as_view(), name="homepage")
]
