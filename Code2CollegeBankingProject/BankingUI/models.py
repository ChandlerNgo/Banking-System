from http.cookiejar import DefaultCookiePolicy
from django.db import models
from django.contrib.auth.models import User

User._meta.get_field("email")._unique = True
User._meta.get_field("username")._unique = True


class Transactions(models.Model):
    date = models.DateField(auto_now_add=True)
    transactiontype = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(User, on_delete=models.CASCADE)
