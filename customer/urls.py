from __future__ import absolute_import
from django.conf.urls import url
from customer.views import RegisterView, Login
__author__ = 'Elfix'

urlpatterns = [
    url(r'new', RegisterView.as_view(), name="register"),
    url(r'login', Login.as_view(), name="login"),
]
