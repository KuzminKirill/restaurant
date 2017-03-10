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

#class Goods(models.Model):
#    title = models.CharField(max_length=250)
#    price = models.IntegerField()
#    description = models.TextField(max_length=200)
#
#    def __str__(self):
#        return self.title


#class Spisok(models.Model):
#    salad = models.OneToOneField(Salad, related_name='+')
#    soup = models.OneToOneField(Soup, related_name='+')
#    main_food = models.OneToOneField(MainFood, related_name='+')
#    decert = models.OneToOneField(Decert, related_name='+')
#    drink = models.OneToOneField(Drink, related_name='+')
#    count = models.IntegerField(default=1)

class Discount(models.Model):
    code = models.CharField(max_length=7)
    coefficient = models.IntegerField(default=1)

    def __str__(self):
        return self.code


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
    discount = models.ForeignKey(Discount, default=0)
    bill = models.IntegerField(default=0)


class Places(models.Model):
    number = models.IntegerField()
    count = models.IntegerField()


class OrderPlaces(models.Model):
    orders_id = models.ForeignKey(Order)
    place_id = models.ForeignKey(Places)

