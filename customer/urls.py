from __future__ import absolute_import
from django.conf.urls import url
from customer.views import RegisterView, Login, ProfileView
__author__ = 'Elfix'

urlpatterns = [
    url(r'new', RegisterView.as_view(), name="register"),
    url(r'login', Login.as_view(), name="login"),
    url(r'profile', ProfileView.as_view(), name="profile"),
    url(r'log-OUT', "customer.views.logout", name="logout"),
]
