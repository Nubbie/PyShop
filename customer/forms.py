from __future__ import absolute_import
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from customer.models import Customer

__author__ = 'Elfix'


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="نام کاربری")
    password1 = forms.CharField(label="گذرواژه دلخواه", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار گذرواژه", widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'phone', 'address')
        model = Customer
        labels = {
            'first_name': "نام",
            'last_name': " نام خانوادگی",
            'phone': "تلفن",
            "address": "آدرس  "
        }

    pass


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    pass
