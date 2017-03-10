from django import forms
from django.contrib.auth.models import User

from .models import Order


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['booking_time', 'salad', 'soup', 'main_food', 'decert', 'drink', 'discount']