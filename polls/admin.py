from django.contrib import admin

from .models import Order, UserDiscount

# Register your models here.

admin.site.register(Order)
admin.site.register(UserDiscount)