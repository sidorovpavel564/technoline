from django.db import models

from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='orders')
    address = models.CharField(max_length=150, verbose_name='Address')
    phone = models.CharField(max_length=25)
    email = models.EmailField(verbose_name='Email', blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    item_price = models.IntegerField(verbose_name='Price')
    quantity = models.PositiveIntegerField(default=1)
    total = models.IntegerField(verbose_name='Total')
