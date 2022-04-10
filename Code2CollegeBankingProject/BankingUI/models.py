from http.cookiejar import DefaultCookiePolicy
from django.db import models

# Create your models here.
class User_Info(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    email = models.EmailField()

class User_Money(models.Model):
    money = models.IntegerField()

class User_Names(models.Model):
    pin_number = models.IntegerField()
    is_admin = models.BooleanField(default="False")
    username = models.CharField(max_length=30)
    info = models.ForeignKey(User_Info,on_delete=models.CASCADE)
    money = models.ForeignKey(User_Money,on_delete=models.CASCADE)
