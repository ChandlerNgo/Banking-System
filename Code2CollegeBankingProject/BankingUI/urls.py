from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("index", views.index, name="index"),
    path("account", views.account, name="account"),
    path("changemoney", views.changemoney, name="changemoney")
]