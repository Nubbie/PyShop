from __future__ import absolute_import
from django.conf.urls import url
from shop.views import Homepage
__author__ = 'Elfix'

urlpatterns = [
    url(r'', Homepage.as_view(), name="homepage")
]
