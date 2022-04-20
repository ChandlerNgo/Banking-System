from http.cookiejar import DefaultCookiePolicy
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Customer(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     birthday = models.DateField()
#     email = models.EmailField()


# class BankInfo(models.Model):
#     pin_number = models.IntegerField()
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=30)
#     customer_info = models.ForeignKey(User, on_delete=models.CASCADE)


class Transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    transactiontype = models.CharField(max_length=8)
    amount = models.IntegerField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)


# ask will to tell me why you cant put all attributes in one table