from __future__ import absolute_import
from django.conf.urls import url
from product.views import ProductList, ProductDetails

__author__ = 'Elfix'

urlpatterns = [
    url(r'^list', ProductList.as_view(), name="Product_List"),
    url(r'^details/(?P<pk>\d+)', ProductDetails.as_view(), name="Product_Details"),
]
