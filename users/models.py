from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    phone_number = models.IntegerField(default='',max_length=15)
    address = models.CharField(default='', max_length=300)
