from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createaccount", views.createaccount, name="createaccount"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("index", views.index, name="index"),
    path("account", views.account, name="account"),
    path("changemoney", views.changemoney, name="changemoney"),
    path("changeaccountinfo", views.changeaccountinfo, name="changeaccountinfo"),
    path("deleteaccount", views.deleteaccount, name="deleteaccount"),
    path("logout_view", views.logout_view, name="logout_view"),
]
