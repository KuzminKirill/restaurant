from django import forms
from django.contrib.auth.models import User
from django.forms import CharField, IntegerField,Textarea
from .models import Order,Soup,Salad,MainFood,Decert,Drink


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['booking_time', 'salad', 'soup', 'main_food', 'decert', 'drink', 'count', 'discount']



#class OrderForm(forms.Form):
#    booking_time = forms.DateField()
#    salad = forms.ModelMultipleChoiceField(queryset=Salad.objects.all())
#    soup = forms.ModelMultipleChoiceField(queryset=Soup.objects.all())
#    main_food = forms.ModelMultipleChoiceField(queryset=MainFood.objects.all())
#    decert = forms.ModelMultipleChoiceField(queryset=Decert.objects.all())
#    drink = forms.ModelMultipleChoiceField(queryset=Drink.objects.all())
#    count = forms.IntegerField()
#    discount = forms.CharField()