from http.cookiejar import DefaultCookiePolicy
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()

class BankInfo(models.Model):
    pin_number = models.IntegerField()
    is_admin = models.BooleanField(default="False")
    username = models.CharField(max_length=30)
    customer_info = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Transactions(models.Model):
    date = models.IntegerField()
    withdrawal_deposit = models.IntegerField()
    amount = models.IntegerField()
    account = models.ForeignKey(BankInfo.id, on_delete=models.CASCADE)
    
# ask will to tell me why you cant put all attributes in one table