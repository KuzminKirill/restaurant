from django.contrib.auth.models import Permission, User
from django.db import models


class Salad(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Soup(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class MainFood(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Decert(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Drink(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class UserDiscount(models.Model):
    show = models.CharField(max_length=10)
    user = models.ForeignKey(User, default=1)
    coefficient = models.FloatField(default=1)

    def __str__(self):
        return self.show


class Order(models.Model):
    user = models.ForeignKey(User, default=1)
    booking_time = models.DateTimeField()
    created_at = models.TimeField(auto_now=True)
    status = models.IntegerField(default=1)
    salad = models.ForeignKey(Salad, related_name='+', default=1)
    soup = models.ForeignKey(Soup, related_name='+', default=1)
    main_food = models.ForeignKey(MainFood, related_name='+', default=1)
    decert = models.ForeignKey(Decert, related_name='+', default=1)
    drink = models.ForeignKey(Drink, related_name='+', default=1)
    count = models.IntegerField(default=1)
    discount = models.ForeignKey(UserDiscount, default=0)
    bill = models.IntegerField(default=0)


class Places(models.Model):
    number = models.IntegerField()
    count = models.IntegerField()


class OrderPlaces(models.Model):
    orders_id = models.ForeignKey(Order)
    place_id = models.ForeignKey(Places)
