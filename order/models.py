from django.db import models
from cart.models import Cart
from users.models import CustomerUser


class order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_address = models.CharField(default='', max_length=300)
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)